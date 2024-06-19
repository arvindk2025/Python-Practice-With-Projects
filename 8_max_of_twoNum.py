def maximum(a, b):
    if(a>=b):
        return a
    else:
        return b


a = int(input("Enter number1 :"))
b= int(input("Enter number 2:"))
print(f'Maximum Number is : {maximum(a,b)}')
