import re
import argparse
from ring import *

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--message", help="Message file")
args = parser.parse_args()


def check(s, n):
    a = []
    b = []
    half = False
    
    for c in s:
        if c == '#':
            half = True
        try:
            if not half:
                a.append(RingInt(int(c), n))
            else:
                b.append(RingInt(int(c), n))
        except:
            continue
    
    left = RingInt(0, n)
    right = RingInt(0, n)
    
    for i in range(len(a)):
        left = left + RingInt(i+1, n) * a[i]
    
    for i in range(len(b)):
        right = right + RingInt(i+1, n) * b[i]
        
    if left == right :
        print("OK")
    else:
        print("CORRUPTED")
        
        
# check("$(1,1,0)#(2,1,1,2)$", 3)

file = open(args.message, "r")
n = file.readline()

message = file.readline()
# print(message)
# codes = re.findall("[0-9]", message)
# codes = re.findall("^\$\(([0-9]+(,[0-9]+)+|[0-9])\)\#\(([0-9]+(,[0-9]+)+|[0-9])\)\$&", message)
codes = re.findall("\$\(\d+(,\d+)", message)


print(codes)

# RegEx: \$\(([0-9]+(,[0-9]+)+|[0-9])\)\#\(([0-9]+(,[0-9]+)+|[0-9])\)\$

# 7
# Hi. Long time since we met each other by dear siss!!! I was reading this book, bought it for $13.99. Found a line - When we were children,
#  Hassan and I used to climb the $(1,0,0,0)#(3,6)$ trees in the driveway of my father's house and annoy our neighbours by reflecting sunlight onto their homes. 
# This reminded me of our childhood. I wish to fly back to $(0,1,0,0,4)#(1)$ once this gets over and buy you and a $(1,1,1,1,1)#(4,4)$. #sis_goals. Signing off $$Sara$$.
