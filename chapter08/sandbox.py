#!/usr/bin/python
# -*- coding: utf-8 -*-


import ctypes
import struct
import os
import sys
import click

SYS_openat = 257

# /usr/include/linux/ptrace.h
PTRACE_TRACEME = 0
PTRACE_PEEKDATA = 2
PTRACE_POKEDATA = 5
PTRACE_GETREGS = 12
PTRACE_SYSCALL = 24


class user_regs_struct(ctypes.Structure):
    _fields_ = [
        ('r15', ctypes.c_ulonglong),
        ('r14', ctypes.c_ulonglong),
        ('r13', ctypes.c_ulonglong),
        ('r12', ctypes.c_ulonglong),
        ('rbp', ctypes.c_ulonglong),
        ('rbx', ctypes.c_ulonglong),
        ('r11', ctypes.c_ulonglong),
        ('r10', ctypes.c_ulonglong),
        ('r9', ctypes.c_ulonglong),
        ('r8', ctypes.c_ulonglong),
        ('rax', ctypes.c_ulonglong),
        ('rcx', ctypes.c_ulonglong),
        ('rdx', ctypes.c_ulonglong),
        ('rsi', ctypes.c_ulonglong),
        ('rdi', ctypes.c_ulonglong),
        ('orig_rax', ctypes.c_ulonglong),
        ('rip', ctypes.c_ulonglong),
        ('cs', ctypes.c_ulonglong),
        ('eflags', ctypes.c_ulonglong),
        ('rsp', ctypes.c_ulonglong),
        ('ss', ctypes.c_ulonglong),
        ('fs_base', ctypes.c_ulonglong),
        ('gs_base', ctypes.c_ulonglong),
        ('ds', ctypes.c_ulonglong),
        ('es', ctypes.c_ulonglong),
        ('fs', ctypes.c_ulonglong),
        ('gs', ctypes.c_ulonglong),
    ]


libc = ctypes.CDLL(None)
ptrace = libc.ptrace


def hook(regs, pid):
    path = b''
    i = 0
    word = b''
    while not b'\x00' in word:
        addr = ctypes.c_ulonglong(regs.rsi + i)
        word = ptrace(PTRACE_PEEKDATA, pid, addr, 0)
        word = struct.pack('<1', word)
        path += word
        i += 4
    path = path[:path.find(b'\x00')].decode()

    if path.startswith('/etc'):
        addr = ctypes.c_ulonglong(regs.rsi)
        data = struct.unpack('<1', b'dum\x00')[0]
        ptrace(PTRACE_POKEDATA, pid, addr, data)


@click.command()
@click.argument('tracee_file')
def run(tracee_file):
    child = os.fork()
    if child == 0:
        ptrace(PTRACE_TRACEME, 0, 0, 0)
        os.execl('/usr/bin/python', 'python', tracee_file)
    else:
        while 1:
            pid, status = os.wait()
            if status != 0:
                regs = user_regs_struct()
                ptrace(PTRACE_GETREGS, pid, 0, ctypes.pointer(regs))

                if regs.orig_rax == SYS_openat:
                    hook(regs, pid)
                    ptrace(PTRACE_SYSCALL, pid, 0, 0)
                else:
                    os._exit(0)


def main():
    run()


if __name__ == '__main__':
    main()
