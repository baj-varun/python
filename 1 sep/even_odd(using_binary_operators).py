#Wap to accept the no. from user and print if it is even or odd without arithmetic op.(use bitwise operators)

x=eval(input("enter any no. of ur chice \n"))

if x&1==0:
    print("the no. is even")
else:
    print("the no. is odd")
