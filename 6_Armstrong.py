num = int(input("Enter the number : "))

sum =0
temp = num
while(temp>0):
    digit = temp%10
    sum = sum+digit**3
    temp = temp//10

if(sum==num):
    print(f"Entered number {num} is Armstrong..")

else:
     print("Entered number {num} is not a Armstrong number..")