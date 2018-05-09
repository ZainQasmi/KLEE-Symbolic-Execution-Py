import sys
from itertools import product
import random

checkIf = [False,False,False,False,False,False]
expr_list = []

def testifs(a,b,c):

	d = a + b -c
	e = a - b
	inter_1 = "d=a+b-c"
	inter_2 = "e=a-b"

	# print "a: ",a,"b: ",b,"c: ",c

	if (d < a+b+c and checkIf[0] == False):
		temp = "d<a+b+c"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

		elif(temp[0]==inter_2[0]):
			temp = inter_2[2:] + temp[1:]
			expr_list.append(temp)

		
		checkIf[0] = True
		return 1

	if (d > a+c-b and checkIf[1] == False):
		temp = "d>a+c-b"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

		checkIf[1] = True
		return 2

	if (d < b-a+c and checkIf[2] == False):
		temp = "d<b-a+c"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

		checkIf[2] = True
		return 3

	if (d > c-a-b and checkIf[3] == False):
		temp = "d>c-a-b"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

		checkIf[3] = True
		return 4

	if (d < c+b+a and checkIf[4] == False):
		temp = "d<c+b+a"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

		checkIf[4] = True
		return 5

	if (d > b+c-a and checkIf[5] == False):
		temp = "d>b+c-a"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

		checkIf[5] = True
		return 6
	
	
	return -1


def main(argv):

	counter = 0
	#password = str(random.randint(0,9999))#example password 
	for i in range(100,1000):    #0-9999
		counter +=1
		Trial = str(i)  
		a = int(Trial[0])
		b = int(Trial[1])
		c = int(Trial[2])
		retVal = testifs(a,b,c)
		
	print len(expr_list)
	for i in range(0,6):
		print expr_list[i]

if __name__ == "__main__":
	main(sys.argv)



