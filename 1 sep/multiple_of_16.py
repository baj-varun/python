#WAP to accept the no. from user and check if it multiple of 16 or not w/o using arithmetic op.

x=eval(input("enter any no. choice \n"))

if x&15==0:
    print(x," is a multiple of 16")
else:
    print(x," is not a multiple of 16")
