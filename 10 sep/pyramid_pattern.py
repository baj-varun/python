"""WAP to the following pattern
      1
    2 1 2
  3 2 1 2 3
4 3 2 1 2 3 4
"""

def pyramid_pattern(x):
    for i in range(1,x+1):
        k=i
        for _ in range(x-i):
            print("\t",end="")

        for l in range(1,2*i):
            print("%d\t"%k,end="")
            if l<i:
                k-=1
            else:
                k+=1
        print("")
                


def main():
    x=eval(input("Enter the no. of rows for which You want to print the pyramid pattern \n"))
    pyramid_pattern(x)


if __name__=="__main__":
    main()
