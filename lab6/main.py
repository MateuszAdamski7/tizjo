#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
   i = 0
   while i < len(format_string):
        if format_string[i:i+2] == "#.":
            j = i + 2
            while j < len(format_string) and format_string[j].isdigit():
                j += 1
            if j < len(format_string) and format_string[j] == 'g':
                width = 0
                if format_string[i+2:j].isdigit():
                    width = int(format_string[i+2:j])
                result = str(int(eval(param)))
                num_zeros = max(0,width - len(result))
                result = "".join(str((int(c) * 9 + 1)%10) for c in result)
                result = "0" * num_zeros + result
                print(result, end="")
                i = j + 1
                continue
        print(format_string[i], end="")
        i += 1
   print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
