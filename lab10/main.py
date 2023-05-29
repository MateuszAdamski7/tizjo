#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    i = 0
    result = ""
    while i < len(format_string):
        if format_string[i] == '#':
            if format_string[i+1] != 'a':
                i += 1
                result += '#'
                continue

            param = int(param)
            width = len(str(param))
            res = int((param*2)/width)
            if(res%2==0):
                result += str(res)
            else:
                result += hex(int(param))[2:]
            i += 2
        else:
            result += format_string[i]
            i += 1
    print(result, end="")
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
