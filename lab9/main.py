#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    i = 0
    width = 0
    result = ""
    while i < len(format_string):
        if format_string[i:i+2] == '#.':
            j = i + 2
            while j < len(format_string) and format_string[j].isdigit():
                j += 1
            if j < len(format_string) and format_string[j] == 'h':
                width = 0
                if format_string[i + 2:j].isdigit():
                    width = int(format_string[i + 2:j])
                else:
                    i -= 1
            res = divmod(param,1)
            new_res = ""
            hel = str(int(res[0]))
            for c in hel:
                if c.isdigit():
                    kod = ord('a') + int(c)
                    lit = chr(kod)
                    new_res += lit

            new_res += '.'

            len_dec = len(str(param)) - len(hel) - 1
            e = str(param)
            aa = e[-len_dec:]
            print(aa)
            iter = 0
            for c in aa:
                if iter >= width:
                    break
                iter += 1
                if c.isdigit():
                    nc = (int(c) + 5) % 10
                    new_res += str(nc)
            hel_len =  width - len(aa)
            if hel_len > 0:
                for c in range(hel_len):
                    new_res += "0"
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
