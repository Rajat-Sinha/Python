#!/bin/python3

import sys

def timeConversion(s):
    st = s.split(':')
    hr = st[0]
    min = st[1]
    sec = st[2]
    if 'AM' in s:
        if hr == '12':
            hr = '00'
        sec = sec.replace('AM',' ')
    elif 'PM' in s:
        if hr == '12':
            hr = '12'
        else:
            hr = int(hr) + 12
        sec = sec.replace('PM',' ')

    return str(hr) + ':' + min + ':' + sec


s = input().strip()
result = timeConversion(s)
print(result)
