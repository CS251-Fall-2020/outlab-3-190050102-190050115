# Enter your code here
import functools

def collapse(L):
	if type(L[0]) is list:
		L.insert(0,'\b')
	s1 = functools.reduce(lambda a,b : a+' '+b if type(b) is str else a+' '+collapse(b),L)
	if type(L[0]) is list:
		L.pop(0)
	return s1

k =  [ ["this","is"], [ ["an", "interesting", "python"], ["programming", "exercise."] ] ]
s = collapse(k)
print(s)