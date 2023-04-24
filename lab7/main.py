#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    i = 0
    result = ""
    while i < len(format_string):
        if format_string[i:i+2] == "#j":	
            temp = hex(int(param))
            new_res = ""
            for c in temp:
                if c in "abcdef":
                    new_res += chr(ord(c)+6)
                else:
                    new_res += c
            result += new_res
            i += 2
        else:
            result += format_string[i]
            i += 1
    print(result,end="")
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
