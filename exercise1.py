How many times will 'hello' be printed?

# 1)
for i in range(3, 17):
    print 'hello'
# prints 14 times hello 

# 2)
for j in range(12):
    if j % 3 == 0:
       print 'hello'
#prints hello 4 times

# 3)
for j in range(15):
	if j % 5 == 3:
		print 'hello'
	elif j % 4 == 3:
		print 'hello'
#prints hello 5 times 
