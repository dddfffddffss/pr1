import random
import math

limit = 1000; p=0

while p<0.995:
	t1ab=0; sumab=0
	for i in range(limit):
		count=0
		while(count<1):
			r=random.random()
			count = count+1 if r>p else 0
			sumab += 1 if r<p else -1
			t1ab+=1
	print("{:.2f}% : E = {:8.3f}, t = {:8.3f}".format(p,sumab/limit,t1ab/limit))
	p+=0.01