#Pattern - 10: Half Diamond Star Pattern
class solution:
    def normal(self,n: int):
        for i in range(1,2*n):
            stars=i
            if i <= n:
                stars=i
            else:
                stars=2*n-i
            print("*"*stars)




if __name__=="__main__":
    sol=solution()
    n=int(input("enter number:"))
    sol.normal(n)
