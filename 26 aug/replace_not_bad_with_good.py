#WAP to accept a string from user and assume that it contains not followed by bad.

string=input("Enter any sring containing bad followed by not \n")

x=string.find("not")
y=string.find("bad")
new=string[x:y+3:1]

print(string.replace(new,"good"))
