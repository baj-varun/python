#wap to accept a string from user; replace the occurence of first character in remaining part of string by * in the remaining string.

x=input("enter a string of ur choice \n")
y=x[0:1:1]

z=x[1::]

z=z.replace(y,"*")
print(y+z)
