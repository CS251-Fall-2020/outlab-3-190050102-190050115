from ring import *


def sum1(k, x):
    sum = RingInt(0, k.characteristic)
    x_pow = RingInt(1, k.characteristic)
    fact = RingInt(1, k.characteristic)
    i = RingInt(1, k.characteristic)
    one = RingInt(1, k.characteristic)
    zero = RingInt(0, k.characteristic)
    
    for j in range(k.value):
        temp = x_pow / fact
        # print(temp, fact, i, j, x_pow)
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
    # print([i.value for i in fact])
    
    prod = RingInt(1, x.characteristic)
    for a in range(k.value):
        sum = RingInt(0, x.characteristic)
        for b in range(a+1):
            # print(self.value + a, b, self.value + a - b)
            try : 
                sum = sum + fact[x.value + a]/(fact[b]*fact[x.value + a - b])
                # print(fact[self.value + a])
                # print((fact[b]*fact[self.value + a - b]))
                # print(sum)
            except ValueError: 
                print("UNDEFINED")
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







   
# x = RingInt(2, 5)
# k = RingInt(4, 5)

# print(x.sum3(k))
 
n = int(input())
 
for i in range(n):           
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    
    k = RingInt(a, c)
    x = RingInt(b, c)

    if d==1:
        print(sum1(k, x))
    elif d==2:
        print(sum2(k, x))
    elif d==3:
        print(sum3(k, x))
    

# print()
# print(x+k)
# print(x-k)
# print(x*k)
# print(x/k)
# print(x**k)

# print( isinstance(5.2, int) )