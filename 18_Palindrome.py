def Palindrome(s):
    rev_s = s[::-1]
    return (s==rev_s)

s = input("Enter string s: ")
flag = Palindrome(s)
if(flag):
    print(f's is Palindrome')
else:
    print(f's is not Palindrome') 