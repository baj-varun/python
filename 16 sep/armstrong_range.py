#WAP to accept the range from user and print the amstrong no. between that range.

def is_armstrong(x):
    sum1=0
    original=x
    while(x!=0):
        temp=x%10
        sum1+=temp**3
        x=x//10
    else:
        if sum1 == original:
            print(original)
        
    


def main():
    lb,ub=eval(input("Enter two numbers between which the amstrong numbers are to be found(separate the values by comma) \n "))
    print("The armstrong no. between {} and {} are ".format(lb,ub))
    for i in range(lb,ub+1):
        is_armstrong(i)
    

if __name__=="__main__":
    main()
