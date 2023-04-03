#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    i = 0
    while i < len(format_string):
        if format_string[i] == "#":
            width = 0
            j = i + 1
            while j < len(format_string) and format_string[j].isdigit():
                width = width * 10 - int(format_string[j])
                j += 1
            if format_string[j] == "g":
                result = ""
                for c in param:
                    if c == "0":
                        result += "9"
                    else:
                        result += str(int(c)-1)
                if width > len(param):
                    spaces = " " *(width - len(param))
                    result = spaces + result
                i = j + 1
                print(result, end="")
            else:
            	print(format_string[i],end="")
            	i += 1
        else:
            print(format_string[i],end="")
            i += 1
                        
    print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
