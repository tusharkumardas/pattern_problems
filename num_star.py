n = 5
mid = n // 2 + 1

#upper half
for i in range(1,mid+1):
    print(" "*(mid-i),end="")
    for j in range(1,i+1):
        print(j,end="")
        if j!=i:
            print("*",end="")
    print()
for i in range(mid-1,0,-1):
    print(" "*(mid-i),end="")
    for j in range(1,i+1):
        print(j,end="")
        if j!=i:
            print("*",end="")
    print()
    

