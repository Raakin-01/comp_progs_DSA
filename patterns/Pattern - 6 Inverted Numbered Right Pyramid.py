def pyramid(n):
    for i in range(n):
        for j in range(i+1,n+1):
            print(n-j+1,end='')
        print()

n=int(input("enter the value:"))
pyramid(n)
