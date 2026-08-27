#Pattern - 12: Number Crown Pattern
class solution:
    def crown(self, n: int):
        for i in range(n):
            for j in range(n):
                print("*",end="")
            print()

if __name__=="__main__":
    sol=solution()
    n=int(input("enter the number:"))
    sol.crown(n)
