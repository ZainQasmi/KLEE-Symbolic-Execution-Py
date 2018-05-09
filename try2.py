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


#########################################################3
## IRRELEVANT AS OF NOW

# left_z3 = []
# def left(l_expr):
# 	left_length = len(l_expr)
# 	# if(left_length==1):
# 	# 	#declare a constant
# 	# 	# (declare-const a Int)
# 	# 	z3_left.append("(")
# 	# 	z3_left.append("declare-const")
# 	# 	z3_left.append(" ")
# 	# 	z3_left.append(l_expr)
# 	# 	z3_left.append(" ")
# 	# 	z3_left.append("Int")
# 	# 	ze_left.append(")")

# 	if(left_length==3):
# 		#a+b => (+ a b)
# 		inter_expr.append("("+l_expr[1]+" "+l_expr[0]+" "+l_expr[2]+")")
# 	else:
# 		return left


# right_z3 = []
# def right(r_expr):
# 	print len(r_expr)
#########################################################3



def count_logical(expressions):
	#checking for greater/less/equal to
	num_logical = []
	pos_logical = []
	time_log = 1
	divide_expr = []

	##expressions[0] = "a+b+c<c+d>e+g"  IF WE HAVE EXPRESSION LIKE THIS, THEN THE FOLLOWING CODE WILL NOT WORK
										##WE NEED TO HANDLE THIS CASE AS WELL
										##UPTILL NOW WE CAN ONLY SOLVE EXPRESSIONS INVOLVING ONE LOGICAL OPERATOR
										##e.g a+b+c<c+d
	for i in range(0,len(expressions)):
		num_logical.append(0) 
		time_log = 1 ##assuming that in each expression there is atleast one logical operator
		for j in range(0,len(expressions[i])):
			if(expressions[i][j]=='>' or expressions[i][j]=='<' or expressions[i][j]=='=='):
				num_logical[i] = num_logical[i] + 1 ##counts the number of logical operators in each 
													##expression and stores it on the corresponding
													##index as to where the expression is stored  
				if(time_log==1): #for the first time a logical operator appears in an expr
					pos_logical.append([]) ##list to store its postion in that whole expression
					time_log = time_log + 1
				pos_logical[i].append(j) ##maintain a list of positions of each logical operator in a single expression
				#print expressions[i][:j] + "|" +  expressions[i][j] + "|"  + expressions[i][(j+1):]

		for k in range(0,num_logical[i]):
			divide_expr.append([]) ## This list will store each expression in broken format
									## e.g if we have a+b+c<c+d. Then this will be stored like 'a+b+c' , '<' , 'c+d'
									## Each expression is broken like this.
			if (num_logical[i]==1): 
				# here the case is handled when there is one logical operator in an expression
				one = expressions[i][:(pos_logical[i][k])] ## e.g storing 'a+b+c'  out of a+b+c<c+d
				operator = expressions[i][pos_logical[i][k]] ## e.g storing '<' out of a+b+c<c+d
				two = expressions[i][(pos_logical[i][k])+1:] ## e.g storing  'c+d' out of  a+b+c<c+d
				divide_expr[i].append(one)
				divide_expr[i].append(operator)
				divide_expr[i].append(two)
				#print expressions[i][:(pos_logical[i][k])] + "----" + expressions[i][(pos_logical[i][k])+1:]
				
			#########################################################
			#########################################################
			## WORK HERE
			elif(num_logical[i]>1): ## THIS IS LEFT. HANDLE THOSE EXPRESSIONS THAT HAVE MORE THAN ONE 
									## LOGICAL OPERATOR e.g a+b+c<c+d>d+e
									## This has to be done like => first solve a+b+c<c+d and then solve (a+b+c<c+d)>d+e
									## But I might be wrong. Have to ask sir.
				get_post = 1 # delete this. it is irrelevant.  

			#########################################################
			#########################################################

	for i in range(0,len(divide_expr)):
		print divide_expr[i]

	# print num_logical
	# print pos_logical

def main(argv):
	final_list = []
	counter = 0
	#password = str(random.randint(0,9999))#example password 
	
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
	## this needs to improved for cases like: a+b<c and a+b<c+a. In this case it will remove the first one
	## although it shouldn't remove it
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
			final_list.append(expr_list[i])

	#print final_list # got the final list of expressions
	count_logical(final_list)

if __name__ == "__main__":
	main(sys.argv)



