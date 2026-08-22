def pyramid(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end='')
        print()

n=int(input("enter the val"))
pyramid(n)
