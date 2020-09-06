import argparse
from ring import *

def sum1(k, x):
    sum = RingInt(0, k.characteristic)
    x_pow = RingInt(1, k.characteristic)
    fact = RingInt(1, k.characteristic)
    i = RingInt(1, k.characteristic)
    one = RingInt(1, k.characteristic)
    zero = RingInt(0, k.characteristic)
    
    for j in range(k.value):
        temp = x_pow/fact
        sum = sum + temp
        
        x_pow = x_pow * x
        fact = fact * i
        i = i + one
    return sum


def sum2(k, x):
    fact = []
    i = RingInt(1, k.characteristic)
    fact_0 = RingInt(1, k.characteristic)
    fact.append(fact_0)
    one = RingInt(1, k.characteristic)
    
    for j in range(1, x.value+k.value+1):
        fact.append( fact[j-1] * i )
        i = i + one
    
    prod = RingInt(1, x.characteristic)
    for a in range(k.value):
        sum = RingInt(0, x.characteristic)
        for b in range(a+1):
            try : 
                sum = sum + fact[x.value + a]/(fact[b]*fact[x.value + a - b])
            except ValueError: 
                # print("UNDEFINED")
                return
        prod = prod * sum
        
    return prod
    

def sum3(k, x):
    sum = RingInt(0, k.characteristic)
    i = RingInt(1, k.characteristic)
    one = RingInt(1, x.characteristic)
    
    for j in range(k.value):
        sum += i ** x
        i = i + one
    
    return sum


parser = argparse.ArgumentParser()
parser.add_argument("-inp", "--input", help="Input File")
parser.add_argument("-out", "--output", help="Output File")
args = parser.parse_args()

in_file = open(args.input, "r")
out_file = open(args.output, "w")

for line in in_file.read().splitlines():
    a, b, m, sum = [int(i) for i in line.split()]
    k = RingInt(a, m)
    x = RingInt(b, m)
    
    if sum==1:
        res = sum1(k, x)
    elif sum==2:
        res = sum2(k, x)
    elif sum==3:
        res = sum3(k, x)
        
    res =  res.__str__()
    out_file.write(res + "\n")
