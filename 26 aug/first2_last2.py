# WAP to accept a string from user and display a string of 1st two and last two characters.

x=input("Enter a string of ur choice \n")
y=x[0:2:1]
z=x[-1:-3:-1]
z=z[::-1]

print(y+z)
