n=8
for i in range(n):
    for j in range(n):
        if j<n-i:
          print(chr(65+j),end=" ")
        else:
            print("#",end=" ")
    for j in range(n-1):
        if j>=i-1:
            print(chr(65+n-j-2),end=" ")
        else:
            print("#",end=" ")
    print()
   
