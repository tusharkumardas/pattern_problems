n=7
mid=n//2+1
for i in range(1,mid+1):
    print(" "*(mid-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    if i>1:
        for j in range(1,i):
            print(j+1,end="")
    print()
for i in range(mid-1,0,-1):
    print(" "*(mid-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    if i>1:
        for j in range(2,i+1):
            print(j,end="")
    print()
        
