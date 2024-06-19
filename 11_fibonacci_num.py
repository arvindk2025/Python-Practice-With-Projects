num = int(input("Enter a number num : "))

n1,n2=0,1
sum=0

if(num<=0):
    print("Please enter a positive number or >0 number")

for i in range(1,num+1):
    print(sum, end=" ")
    n1 = n2
    n2=sum
    sum = n1+n2


