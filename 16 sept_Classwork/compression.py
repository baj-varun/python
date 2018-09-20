#Wap to accept a string from user and perform compression on the same.

def compress(x):
    count = 1
    temp = ""
    k=x[0]
    for i in range(len(x)):
        if(i == (len(x)-1)):
            temp=temp+k+str(count)
            continue

        if k == x[i+1]:
            count=count+1
        else: 
            temp = temp+k+str(count)
            k=x[i+1]
            count=1
    else:
        print(temp)
            
            
    
def main():
    string = input("Enter the string containing consecutive repitive characters and to perform compression \n")
    compress(string)
    
if __name__=="__main__":
    main()

