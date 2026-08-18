class solution:
    def pattern1(self,N):
        for i in range(N):
            for j in range(N):
                print("*",end="")
            print()

sol=solution()
N=5
sol.pattern1(N)
