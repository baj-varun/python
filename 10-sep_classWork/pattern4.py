"""WAP to print following pattern(no. of rows = no. of stars)
* * * *
  * * *
    * *
      *

"""



def pattern1(x):
    for i in range(x,0,-1):
        for _ in range(x-i):
            print("\t",end="")
        for _ in range(i):
            print("*\t",end='')
        print("")
        

def main():
    rows=eval(input("Enter the no. of rows to be printed for the pattern \n"))
    pattern1(rows)

if __name__=="__main__":
    main()
