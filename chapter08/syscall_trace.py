#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes
import os
import sys
import click


PTRACE_TRACEME = 0
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


@click.command()
@click.argument('tfile')
def run(tfile):
    libc = ctypes.CDLL(None)
    ptrace = libc.ptrace

    tracee_file = tfile
    child_pid = os.fork()
    if child_pid == 0:
        ptrace(PTRACE_TRACEME, 0, 0, 0)
        os.execl('/usr/bin/python', 'python', tracee_file)
    else:
        while 1:
            pid, status = os.wait()
            if status != 0:
                regs = user_regs_struct()
                ptrace(PTRACE_GETREGS. pid, 0, 0)
            else:
                sys.exit(0)


def main():
    run()


if __name__ == '__main__':
    main()
