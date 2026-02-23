n=int(input("Enter thr number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==n+1-i:
            print(min(i,n+1-i),end=" ")
        else:
            print(0,end=" ")
    print()
