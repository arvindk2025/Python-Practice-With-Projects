
def maximum(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif (c>a and c>b):
        return c


a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))

print(f'maximum number is : {maximum(a,b,c)}')