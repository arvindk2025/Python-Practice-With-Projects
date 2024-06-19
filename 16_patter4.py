def pattern4(n):
    num = 65
    for i in range (0, n):
        ch = chr(num)
        for j in range(0, i+1):
            print(f'{ch}', end="")
             
        num+=1
        print("\r")

n = 5
pattern4(n)