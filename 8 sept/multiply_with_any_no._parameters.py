#Write a function to multiply any no. of numbers.

def multiply(*args):
    result=1
    for i in args:
        result=result*i
    else:
        print(result)

multiply(2,3,5)
multiply(5,7,20,45)
    
