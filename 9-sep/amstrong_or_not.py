# WAP to accept a no. from user and check if its an amstrong no.

def isAmstrong(x):
    sum=0
    original=x
    while(x!=0):
        temp=x%10
        sum+=temp**3
        x=x//10
    else:
        if sum == original:
            return True
        else:
            return False
        
def main():
    x=eval(input("enter any no. of ur choice \n"))
    if isAmstrong(x):
        print("%d is the amstrong no."%x)
    else:
        print("%d is not an amstrong no."%x)
    
    

if __name__=="__main__":
    main()
