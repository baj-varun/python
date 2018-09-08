# WAP to accept a no. from user and check whether the no. is multiple of 128 or not.

x=eval(input("enter any no. choice \n"))

if x&127==0:
    print(x," is a multiple of 128")
else:
    print(x," is not a multiple of 128")
