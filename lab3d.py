#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space'''
# Author ID: mepalaypay1

import subprocess

def free_space():
    process = subprocess.Popen(
        ['df', '-h', '/'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    output = stdout.decode('utf-8').strip()
    lines = output.splitlines()
    root_line = lines[1]
    free_space_value = root_line.split()[3]
    return free_space_value

if __name__ == '__main__':
    print(free_space())