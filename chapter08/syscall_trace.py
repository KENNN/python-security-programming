#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes
import os
import sys
import click


PTRACE_TRACEME = 0
PTRACE_GETREGS = 12
PTRACE_SYSCALL = 24


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
