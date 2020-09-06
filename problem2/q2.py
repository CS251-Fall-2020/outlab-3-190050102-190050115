# Enter your code here
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-inp','--infile',help="input")
parser.add_argument('-out','--outfile',help="output")
args = parser.parse_args()

f = open(args.infile,"r")
lines = f.read().splitlines()
path = lines[0]

f.close()

dirlist = []

for i in range(0,len(path)):
	s = ""
	if path[i] == '/':
		i+=1
		while (i<len(path) and path[i]!='/'):
			s+=path[i]
			i+=1
	if(s =='.' or s==''):
		continue
	elif(s =='..'):
		if(len(dirlist)!=0):
			dirlist.pop()
	else:
		dirlist.append(s)

canonpath=''

if(len(dirlist)== 0):
	canonpath+='/'
else:
	for i in range(0,len(dirlist)):
		canonpath+='/'
		canonpath+=dirlist[i]
		

f1 = open(args.outfile,'w')
f1.write(canonpath)
f1.close()


