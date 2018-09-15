"""
WAP to the following pattern
      A
    B A B
  C B A B C
D C B A B C D
"""

def pattern1(x):
        for i in range(1,x+1):
                k=64+i
                for _ in range(x-i):
                        print("\t",end="")
                for l in range(1,2*i):
                        print(chr(k)+"\t",end="")
                        if l<i:
                                k-=1
                        else:
                                k+=1
                print("")
                

def main():
    rows=eval(input("Enter the no. of rows to be printed for the pattern \n"))
    pattern1(rows)

if __name__=="__main__":
    main()
