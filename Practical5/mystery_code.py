# What does this piece of code do?
# Answer: from (1,100),get a number randomly. If it is bigger than 50, get another random number from (1,100) until the number is under or equal to 50. print this final number.  

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# define that p is false.
# when p is false, run the following code
#   define p is true
#   n is a random integer chosen from (1,100)
#   if n is bigger than 50, p is defined as false and run again
#   if n is not bigger than 50, print out the value of n. 

p=False
while p==False:
	p = True
	n = randint(1,100)
	if n > 50:
		p = False

print(n)
