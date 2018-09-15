#WAP to accept a no. from user and print its reverse.


def reverse(x):
    num=0
    while(x!=0):
        temp=x%10
        num=num*10+temp
        x=x//10
    else:
        return num
    
    
def main():
    x=eval(input("enter any no. of ur choice to print it's reverse \n"))
    print("The reverse of %d is %d"%(x,reverse(x)))


if __name__=="__main__":
    main()
