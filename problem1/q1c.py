from ring import *

class Series:
	def __init__():
		sm = RingInt(0, k.characteristic)
        x_pow = RingInt(1, k.characteristic)
        fact = RingInt(1, k.characteristic)
        i = RingInt(1, k.characteristic)
        one = RingInt(1, k.characteristic)
        zero = RingInt(0, k.characteristic)

    def __iter__():
    	return x_pow/fact

    def __next__():
    	sum = sum + temp
            
        x_pow = x_pow * self
        fact = fact * i
        
        i = i + one

        return x_pow/fact



def main():

	in_str = str(input())
	in_list = in_str.split(' ')
	k, x, n = in_list[0], in_list[1], in_list[2]
	
	for ele in Series(k, x, n):
		print(ele)


if __name__=="__main__":
	main()

