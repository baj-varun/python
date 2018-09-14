#WAP to accept a no. from user and display even digits sum and odd digits sum.(and display the difference of odd sum and even sum)


def evenOdd_sum(x):
    even_sum=0
    odd_sum=0
    while(x!=0):
        temp=x%10
        if temp%2==0:
            even_sum+=temp
        else:
            odd_sum+=temp
        x=x//10
    else:
        print("The even digits sum of given no. is {}".format(even_sum))
        print("The odd digits sum of given no. is {}".format(odd_sum))
        if even_sum>odd_sum:
            difference=even_sum - odd_sum
        else:
            difference=odd_sum - even_sum
        print("The difference between the even digits sum and odd digits sum of given no. is {}".format(difference))
        
def main():
    x=eval(input("enter any no. of ur choice \n"))
    evenOdd_sum(x)
    
    

if __name__=="__main__":
    main()
