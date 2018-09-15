"""WAP to print a generic pattern as follows:
A
A A
A A A
A A A A
where there can be any character of number in place of 'A' as per users choice.
"""

def generic_pattern(x,sym):
    for i in range(1,x+1):
        for _ in range(i):
            print(sym+"\t",end="")
        print("")
    
    

def main():
    rows=eval(input("Enter the no. of rows for which u want to print the pattern \n"))
    character=input('Enter the character u want in the pattern\n')
    print("")
    generic_pattern(rows,character)
    
    
if __name__=="__main__":
    main()
