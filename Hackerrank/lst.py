if __name__ == '__main__':
    N = int(input())
    act_val=[]
    for _ in range(N):
       func,*val=input().split()
       amt=list(map(int,val))
       if func=="insert":
           act_val.insert(amt[0],amt[1])
       elif func =="print":
           print(act_val)
       elif func =="sort":
           act_val.sort()
       elif func=="remove":
           act_val.remove(amt[0])
       elif func == "append":
           act_val.append(amt[0])
       elif func =="pop":
           act_val.pop()
       elif func =="reverse":
           act_val.reverse()
