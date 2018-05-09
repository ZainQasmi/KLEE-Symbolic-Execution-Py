import sys
from itertools import product
import random

hits = []
expr_list = []

def testifs(a,b,c):

	d = a + b -c
	e = a - b
	inter_1 = "d=a+b-c"
	inter_2 = "e=a-b"

	# print "a: ",a,"b: ",b,"c: ",c

	if (d < a+b+c):
		temp = "d<a+b+c"
		if temp not in hits:

			hits.append(temp)
			if(temp[0]==inter_1[0]):
				temp = inter_1[2:] + temp[1:]
				expr_list.append(temp)

			elif(temp[0]==inter_2[0]):
				temp = inter_2[2:] + temp[1:]
				expr_list.append(temp)

			
			return 1

	if (d > a+c-b):
		temp = "d>a+c-b"
		if temp not in hits:
			hits.append(temp)
			if(temp[0]==inter_1[0]):
				temp = inter_1[2:] + temp[1:]
				expr_list.append(temp)

			return 2

	if (d < b-a+c):
		temp = "d<b-a+c"

		if temp not in hits:
			hits.append(temp)
			if(temp[0]==inter_1[0]):
				temp = inter_1[2:] + temp[1:]
				expr_list.append(temp)

			return 3

	if (d > c-a-b):
		temp = "d>c-a-b"

		if temp not in hits:		
			hits.append(temp)
			if(temp[0]==inter_1[0]):
				temp = inter_1[2:] + temp[1:]
				expr_list.append(temp)

			return 4

	if (d < c+b+a):
		temp = "d<c+b+a"

		if temp not in hits:
			hits.append(temp)
			if(temp[0]==inter_1[0]):
				temp = inter_1[2:] + temp[1:]
				expr_list.append(temp)
			return 5

	if (d > b+c-a):
		temp = "d>b+c-a"

		if temp not in hits:
			hits.append(temp)
			if(temp[0]==inter_1[0]):
				temp = inter_1[2:] + temp[1:]
				expr_list.append(temp)

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



