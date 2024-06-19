num = int(input("Enter the digit : "))

temp = num
reverse = 0

while (temp>0):
   remainder = temp%10
   reverse = reverse*10+remainder
   temp = temp//10

if(num==reverse):
   print(f'Enter digit {num} is Palindrome....')
else:
   print(f'Enter digit {num} is not Palindrome..')