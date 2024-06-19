def check(s1, s2):
    if(sorted(s1)==sorted(s2)):
        print(f'{s1} and {s2} are anagram..')
    else:
        print(f'{s1} and {s2} are not anagram..')

s1 = input("String s1: ")
s2 = input("String s2: ")
check(s1,s2)