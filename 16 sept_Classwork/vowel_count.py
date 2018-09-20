#WAP to accept a string from user and return the count of vowels from the string

def count_vowels(x):
    count=0
    vowels="aeiouAEIOU"
    for i in range(len(x)):
        if x[i] in data:
            count+=1
    else:
        print("the no. of vowels is {}".format(count))

def main():
    string=(input("Ente any string from the user \n"))

if __name__=="__main__":
    main() 
