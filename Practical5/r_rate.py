# define r is the average number of individuals infected by each individual with the virus.(r)
# define there are 84 infected people originally.(n)

r = 1.2
n = 84

# in each loop,  n = r * n + n
# after 5 rounds, print n

for i in range(1,5):
	n = r * n + n

print (" with the r rate equal to 1.2, the total number of individuals infected after 5 generations is" + str(n))


