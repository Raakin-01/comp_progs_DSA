#Pattern - 8: Inverted Star Pyramid
class solution:
    def pyramid(self,n):
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
    n=int(input("enter the value:"))
    sol.pyramid(n)
