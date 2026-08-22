def pyramid(N):
    for i in range(N+1):
        for j in range(i):
            print(i,end='')
        print()

a=int(input("enter thr number:"))
pyramid(a)
