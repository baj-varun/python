__name__ = "__main__":
	x=input("Enter the 1st string \n")
	a=input("Enter the 2nd string \n")
	y=x[0:2:1]
	z=x[len(x)-1:1:-1]
	z=z[::-1]

	b=a[0:2:1]
	c=a[len(a)-1:1:-1]
c=c[::-1]

x=y+c
a=b+z

print("After jumbling, the results are: " + x +" and "+ a)




