def pattern6(n):
    num =65
    for i in range (0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(f'{ch}', end="")
            num+=1
        print("\r")
n=5
pattern6(n)