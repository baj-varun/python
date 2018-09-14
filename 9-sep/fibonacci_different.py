def dis_fibonacci(x):
    c=0
    a,b=0,1
    print(a,b,end=" ",sep=" ")
    while True:         
        c=a+b
        if(c>x):
            break
        else:
            print(c,end=" ")
            a=b
            b=c
        
        

def main():
    x=eval(input("enter the no. such that the value in the fibonacci series should not exceed that number \n"))
    dis_fibonacci(x)

if __name__=="__main__":
    main()
