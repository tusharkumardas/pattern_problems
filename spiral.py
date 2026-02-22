n=4

matrix=[[0]*n for _ in range(n)]

top=0
bottom=n-1
left=0
right=n-1

num=1

while top <= bottom and left<=right:
    #move left to right
    for i in range(left,right+1):
        matrix[top][i]=num
        num+=1
    top+=1
     #move top to bottom
    for i in range(top,bottom+1):
        matrix[i][right]=num
        num+=1
    right-=1

    #move right to left
    if top<=bottom:
        for i in range(right,left-1,-1):
            matrix[bottom][i]=num
            num+=1
        bottom-=1
    #move bottom to top
    if left<=right:
        for i in range(bottom,top-1,-1):
            matrix[i][left]=num
            num+=1
        left+=1
#print rows of the matrix        
for rows in matrix:
   print(*rows)
