num = int(input("Enter the number n: "))

if(num<0):
    print(f'Factorial does not exist for {num}')
elif(num==0):
    factorial= 1
    print(f'factorial of {0} : {factorial}')

else:
    factorial=1
    for i in range (1, num+1):
        factorial = factorial*i

print(f'Factorial of {num} is : {factorial}')