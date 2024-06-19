num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if(num1<num2):
    mini =  num1
else:
    mini= num2

for i in range (1, mini+1):
    if(num1%i==0 and num2%i==0):
        hcf_or_gcd = i


print(f"GCD_OR_HCF of {num1} and {num2} is : {hcf_or_gcd}")