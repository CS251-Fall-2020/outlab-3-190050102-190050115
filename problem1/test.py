from ring import *

# while True:
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

k = RingInt(a, c)
x = RingInt(b, c)

# print(x.sum2(k))
print(k/x)