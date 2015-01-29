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
#prints when numbers 0-11 are divisble by 3 

# 3)
for j in range(15):
	if j % 5 == 3:
		print 'hello'
	elif j % 4 == 3:
		print 'hello'
#prints hello 5 times and prints hello when numbers from 0-14 and not divisible by 5
# and have a remainder of 3

# 4)
z=0
while z != 15:
	print 'hello'
	z=z+3
#prints "hello" 5 times
# prints hello when z isn't 15. and stops when z=15

# 5)
z = 12
while z < 100:
	if z == 31:
		for k in range(7):
			print 'hello'
	elif z == 18:
		print 'hello' 
	z=z+1

#prints hello 8 times and
# while z is less then 100, if z equals 31 then it'll print hello 7 times

def foo1(x):
    return x ** 0.5

#what does foo do? 
#it defines the function of x and takes the squarroot of it 

def foo2(x, y): 
	ifx>y:
￼￼￼   return x
	return y
#it defines a function and foo2 and its 2 variables x and y if x>y then it'll return
# y or it'll print y 

def foo3(x, y, z):
	if x > y:
		tmp = y
		y=x
		x = tmp
	if y > z:
		tmp = z
		z=y
		y = tmp
	if x > y:
		tmp = y
		y=x
		x = tmp
	return [x, y, z]

#makes a function with 3 variables and if x>y then x and y will switch 
# if y>z and then y and z will switch 



