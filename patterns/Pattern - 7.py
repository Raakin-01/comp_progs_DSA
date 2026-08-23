#Pattern - 7: Star Pyramid
def pyramid(n):
    for i in range(n-1):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end="")
        print()

n=int(input("enter the number:"))
pyramid(n)
