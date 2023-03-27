#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    i=0;
    result=""
    result1=""
    while i < len(format_string):
        result = ""
        result1 = ""
        if format_string[i] == '#':
            if format_string[i+1] == "g":
                result += str(int(eval(param)))
                num = str(result[::-1])
                result1 += num
                i += 2
                print(result1, end="")
            else:
                print("#",end="")
                i += 1
        else:
            print(format_string[i], end="")
            i += 1
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
