#WAP to accept a no. from user and check if it is a palindrome number.


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
    rev=reverse(x)
    if rev==x:
        print("%d is a palindrome number"%x)
    else:
        print("{} is not a palindrome number".format(x))


if __name__=="__main__":
    main()
