#Pattern - 9: Diamond Star Pattern
class solution:
    def normal(self,n):
        for i in range(n-1):
            for j in range(n-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            for j in range(n-i-1):
                print(" ",end="")
            print()

    def inverted(self,n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for j in range(2*n-(2*i+1)):
                print("*",end="")
            for j in range(i):
                print(" ",end="")
            print()


if __name__=="__main__":
    sol=solution()
    n=int(input("Enter the number for input:"))
    sol.normal(n)
    sol.inverted(n)
