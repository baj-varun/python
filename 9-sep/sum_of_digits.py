def sum_of_digits(x):
    sum=0
    while(x!=0):
        temp=x%10
        sum+=temp
        x=x//10
    else:
        print("The sum of the digits of the given no. is {0}".format(sum))
        
def main():
    x=eval(input("enter any no. of ur choice \n"))
    sum_of_digits(x)
    

if __name__=="__main__":
    main()
