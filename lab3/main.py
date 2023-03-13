#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    shouldDo=True
    lastK = False
    res = ''
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.':
            	lastK = False
            	idx=idx+2
            	res = ''
            	while(format_string[idx]>='0' and format_string[idx]<='9'):
            		res = res + format_string[idx]
            		idx = idx + 1
            	if format_string[idx] == "k":
            		lastK = True
            		counter = int(res)
            		if counter > len(param):
                        	print(param.swapcase(),end="")
                        	shouldDo=False
                        	continue
            		for i in range(0, counter):
                		print(param[i].swapcase(),end="")
                		shouldDo=False
            else:
            	if lastK:
            		idx = idx + 2
            	if idx >= len(format_string):
                    break	
            	print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
