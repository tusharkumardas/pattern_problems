#print a cuboid with same numbers at the bottom
n=5
#left part
for i in range(n):
    for j in range(n):
        if j<=i:
            print(n-j,end=" ")
        else:
            print(n-i,end=" ")
#right part
    for j in range(2,-1,-1):
        if j<=i:
            print(n-j,end=" ")
        else:
            print(n-i,end=" ")
    print()
#lower left part
for i in range(n-2,-1,-1):
    for j in range(n):
        if j<=i:
            print(n-j,end=" ")
        else:
            print(n-i,end=" ")
    for j in range(2,-1,-1):
        if j>=i:
            print(n-i,end=" ")
        else:
            print(n-j,end=" ")
    print()
    
        
        
