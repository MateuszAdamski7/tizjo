#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    i = 0
    result = ""
    counter = 0
    while i < len(format_string):
        if format_string[i] == '#':
            if format_string[i+1] != 'b':
                i += 1
                result += '#'
                continue

            param = int(param)
            binary = format(param, 'b')
            reversed_binary = str(binary)
            reversed_binary = reversed_binary[::-1]
            res = ""
            for c in reversed_binary:
                if c == '1':
                    if counter == 10:
                        counter = 0
                    res += chr(ord(c) + 48 + counter)
                else:
                    res += c
                counter += 1
            result += res[::-1]
            i += 2
        else:
            result += format_string[i]
            i += 1
    print(result, end="")
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
