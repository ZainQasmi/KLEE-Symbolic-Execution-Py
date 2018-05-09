import sys
from itertools import product
import random

expr_list = []

def testifs(a,b,c):

	d = a + b -c
	e = a - b
	inter_1 = "d=a+b-c"
	inter_2 = "e=a-b"

	# print "a: ",a,"b: ",b,"c: ",c

	if (d < a+b+c):
		temp = "d<a+b+c"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

		elif(temp[0]==inter_2[0]):
			temp = inter_2[2:] + temp[1:]
			expr_list.append(temp)

	if (d > a+c-b):
		temp = "d>a+c-b"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

	if (d < b-a+c):
		temp = "d<b-a+c"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

	if (d > c-a-b):
		temp = "d>c-a-b"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

	if (d < c+b+a):
		temp = "d<c+b+a"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)

	if (d > b+c-a):
		temp = "d>b+c-a"
		if(temp[0]==inter_1[0]):
			temp = inter_1[2:] + temp[1:]
			expr_list.append(temp)





def main(argv):

	counter = 0
	#password = str(random.randint(0,9999))#example password 
	# s1 = 0
	# s2 = 1
	# check = 0
	for i in range(100,1000):    #0-9999
		
		counter +=1
		Trial = str(i)  
		a = int(Trial[0])
		b = int(Trial[1])
		c = int(Trial[2])
		retVal = testifs(a,b,c)

	s1=0
	s2=0
	check=0
	for j in range (s1,len(expr_list)):
		for k in range(s2,len(expr_list)):
			if(j==k):
				fazul = 1
			else:
				l_s1 = len(expr_list[j])
				l_s2 = len(expr_list[k])
				if(l_s1>l_s2):
					for x in range(0,l_s2):
						if(expr_list[j][x]==expr_list[k][x]):
							check = check + 1

					if (check==l_s2):
						expr_list[k] = "@"
				
				elif(l_s1<=l_s2):
					for x in range(0,l_s1):
						if(expr_list[j][x]==expr_list[k][x]):
							check=check+1

					if(check==l_s1):
						expr_list[j]="@"

				check = 0

	for i in range(0,len(expr_list)):
		if(expr_list[i]=="@"):
			fazul = 1
		else:
			print expr_list[i]

if __name__ == "__main__":
	main(sys.argv)



