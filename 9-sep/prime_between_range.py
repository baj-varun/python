def isPrime(a):
    if a<2:
        return False
    elif a==2 or a==3:
        return True
    elif a%2==0:
        return False
    else:
        for i in range(3,(a//2)+2,2):
            if a%i==0:
                return False
        else:
            return True



def main():
    x,y=eval(input("enter the numbers to find the prime numbers between those numbers (type the numbers separated by comma) \n"))
    print("The prime numbers between {} and {} are: \n".format(x,y))
    for i in range(x,y+1):
        if isPrime(i):
            print(i)

if __name__=="__main__":
    main()
