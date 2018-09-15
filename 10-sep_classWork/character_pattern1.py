"""
WAP to the following pattern
A
A B
A B C
A B C D
"""

def pattern1(x):
    for i in range(1,x+1):
        for j in range(i):
            print(chr(65+j)+"\t",end='')
        print("")
        

def main():
    rows=eval(input("Enter the no. of rows to be printed for the pattern \n"))
    pattern1(rows)

if __name__=="__main__":
    main()
