n=7
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    for j in range(i,n+1):
        print(j,end=" ")
    print()
for i in range(2,n+1):
    print(" "*(n-i),end=" ")
    for j in range((n-i)+1,n+1):
        print(j,end=" ")
    print()
