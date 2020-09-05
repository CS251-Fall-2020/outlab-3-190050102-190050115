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
        
    # def __truediv__(self, other):
    #     inv = self.__mod_inv(other.value, self.characteristic)
    #     if inv == -1:
    #         raise ValueError("UNDEFINED")
    #         return "UNDEFINED"
    #         # print("UNDEFINED")
    #         # return ValueError
    #     else:
    #         print(inv)
    #         r = RingInt( (inv * self.value) % self.characteristic , self.characteristic )
    #         return r
    
    def __truediv__(self, other):
        res = (self.value + self.value*self.characteristic) / other.value
        res = res % self.characteristic
        
        return RingInt(int(res), self.characteristic)

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
        g = self.__gcd(b, m)  
        if (g != 1): 
            # return ValueError
            raise ValueError("UNDEFINED")
            return
        else:
            return pow(b, m - 2, m) 
    
