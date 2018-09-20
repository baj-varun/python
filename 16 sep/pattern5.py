"""WAP to print the following pattern
	*   *
	** **
	*****
""""

def pattern5():
    for i in range(1,4):
        count=0
        for _ in range(i):
            print("*\t",end="")
            count+=1
        for _ in range(5-2*i):
            print("\t",end="")
            count+=1
        for _ in range(5-count):
            print("*\t",end="")
        print("")
            




def main():
    print("The required pattern is:\n")
    pattern5()


if __name__=="__main__":
    main()
