from z3 import *

s = Solver()
a = Int('a')
b = Int('b')
c = Int('c')

try:
	f = open("data.txt","r")
	try:
		for l in f:
			s.add(eval(l))
	finally:
		f.close()
except IOError:
	pass

for c in s.assertions():
    print c
print s.check()

try:
	m = s.model()
	print m
except:
	print "CASE FAILED: the constraints were unsolvable."
