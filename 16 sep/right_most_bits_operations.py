#WAP to accept a no. from user and no. of bits to turn on from the right most side. Turn on respective rightmost bits(also toggle and turn off)

def turn_on_right(no,y):
    temp=(2**y)-1
    #temp=(1<<y)-1
    print("The given no. is {}".format(bin(no)))
    sol= no|temp
    print("The no. after turning on the right {} bits from {} i.e {} is {} i.e {}".format(y,no,bin(no),sol,bin(sol)))

def turn_off_right(no,y):
    temp=(2**y)-1
    #temp=(1<<y)-1
    print("The given no. is {}".format(bin(no)))
    sol= no&(~temp)
    print("The no. after turning off the right {} bits from {} i.e {} is {} i.e {}".format(y,no,bin(no),sol,bin(sol)))

def toggle(no,y):
    temp=(2**y)-1
    #temp=(1<<y)-1
    print("The given no. is {}".format(bin(no)))
    sol= no^temp
    print("The no. after toggling the right {} bits from {} i.e {} is {} i.e {}".format(y,no,bin(no),sol,bin(sol)))



def main():
    number=eval(input("Enter the number of ur choice \n"))
    right_most=eval(input("enter the no. of bits to turn on from rightside \n"))
    print("")
    turn_on_right(number,right_most)
    turn_off_right(number,right_most)
    toggle(number,right_most)

if __name__=="__main__":
    main()
