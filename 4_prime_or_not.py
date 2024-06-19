num = int(input('Enter the number n : '))
if (num>1):
    flag = False
    for i in range(2, num):
        if(num%i==0):
            flag = True
    
if(flag):
    print(f'{num} is prime not a number.')

else:
     print(f'{num} is prime number.')