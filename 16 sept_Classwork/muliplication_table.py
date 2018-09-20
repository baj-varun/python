def mult_table(x):
    print("{}'s table :".format(x))
    for i in range(1,11):
        print("{} * {} = {}".format(x,i,(x*i)))
    print("")

def main():
    lb,ub=eval(input("Enter the lower and upper bound to print their multiplication tables \n"))
    for i in range(lb,ub+1):
        mult_table(i)
    

if __name__=="__main__":
    main()
