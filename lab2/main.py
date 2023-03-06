#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    res = ''
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.':
            	idx=idx+2
            	res = ''
            	while(format_string[idx]>='0' and format_string[idx]<='9'):
            		res = res + format_string[idx]
            		idx = idx + 1
            	if format_string[idx] == "k":
            		counter = int(res)
            		for i in range(0, counter):
                		print(param[i].swapcase(),end="")
                		shouldDo=False
            else:
            	
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
