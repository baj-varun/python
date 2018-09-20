"""WAP to print the following pattern
         *
	***
       *****
	***
	 *
"""

def pattern_6():
    for i in range(1,6):
        if i==4:
            i=2
        if i==5:
            i=1
        for _ in range(3-i):
            print("\t",end="")
        for _ in range(2*i-1):
            print("*\t",end="")
        
        print("")
            
            


def main():
    print("The required pattern is as follows: \n")
    pattern_6()


if __name__=="__main__":
    main()
