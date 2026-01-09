#print inverted V pattern using alphabets
def invertedV(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(i+1):
            if j==0:
                print(chr(65+n-1-i),end=" ")
            else:
                print(" ",end=" ")
        for j in range(i):
            if j==i-1:
                print(chr(65+n-1-i),end=" ")
            else:
                print(" ",end=" ")
        print()
invertedV(5)
            
