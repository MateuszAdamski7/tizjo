#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    i = 0
    width = 0
    result = ""
    while i < len(format_string):
        if format_string[i:i+2] == '#.':
            j = i + 2
            while j < len(format_string) and format_string[j].isdigit():
                j += 1
            if j < len(format_string) and format_string[j] == 'j':
                width = 0
                if format_string[i + 2:j].isdigit():
                    width = int(format_string[i + 2:j])
                else:
                    i -= 1    
            p = hex(int(param))[2:]
            new_res = ""
            for c in p:
                if c in "abcdef":
                    new_res += chr(ord(c)+6)
                else:
                    new_res += c

            num_zeros = max(0,width - len(new_res))
            new_res = "0" * num_zeros + new_res
            new_res = new_res.replace('0', 'o')
            result += new_res

            i += 3 + len(str(width))
            continue
        else:
            result += format_string[i]
            i += 1
    print(result, end="")
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
