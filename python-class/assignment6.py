def add_function (x=1,y=1):
    x = input("Type a number: ")
    y = input("Type another number: ")
    sum = int(x) + int(y)
    print("The sum is: ", sum)
    return x, y

add_function()