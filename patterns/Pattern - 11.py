#Pattern - 11: Binary Number Triangle Pattern
class solution:
    def triangle(self,n : int):
        for i in range(1,n+1):
            for j in range(i):
                if((i+j)%2!=0):
                    print(1,end="")
                else:
                    print(0,end="")
            print()

if __name__=="__main__":
    sol=solution()
    n=int(input("enter the number :"))
    sol.triangle(n)
