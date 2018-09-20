
def is_special(x):
    fact=1
    for i in range(2,x+1):
        fact=fact*i
    else:
        print(fact)
        if fact==x:
            print("%d is aspecial_no.")


def main():
    x=eval(input("Enter the number of ur choice to check for special no."))
    is_special(x)

if __name__=="__main__":
    main()
