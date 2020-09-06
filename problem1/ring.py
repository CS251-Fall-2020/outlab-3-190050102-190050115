class RingInt:
    def __init__(self, value, characteristic):
        self.characteristic = characteristic
        self.value = value
        
    def __str__(self):
        return "{}[{}]".format(self.value, self.characteristic)
    
    def __add__(self, other):
        return RingInt((self.value + other.value)%self.characteristic, self.characteristic)
    
    def __sub__(self, other):
        return RingInt((self.value - other.value)%self.characteristic, self.characteristic)
    
    def __mul__(self, other):
        return RingInt((self.value * other.value)%self.characteristic, self.characteristic)
        
    def __truediv__(self, other):
        inv = self.__mod_inv(other.value, self.characteristic)
        # print(inv)
        if inv == -1:
            raise ValueError
            return "UNDEFINED"
        else:
            r = RingInt( (inv * self.value) % self.characteristic , self.characteristic )
            return r

    def __pow__(self, other):
        return RingInt((self.value ** other.value )%self.characteristic, self.characteristic)
    
    def __eq__(self, other):
        if self.value == other.value and self.characteristic == other.characteristic:
            return True
        return False
    
    def __gcd(self, a, b):
        if a==0:
            return b
        if b==0:
            return a
        
        if a==b:
            return a
        
        if a>b:
            return self.__gcd(a-b, b)
        else:
            return self.__gcd(a, b-a)
    
    def __mod_inv(self, b, m):
        if b==0:
            return m
        for i in range(m):
            if( (b*i)%m == 1):
                return i  

        raise ValueError
        return "UNDEFINED"
