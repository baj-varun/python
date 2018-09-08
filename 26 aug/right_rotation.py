#WAP to accept two strings from user and check if the second string is right rotation of first.
#	eg. manager
#	o/p: germana

x=input("Enter the 1st string \n")
a=input("Enter the 2nd string \n")

z=x+x
if a in z:
    print(a, "is right rotation of", x)

