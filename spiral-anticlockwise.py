n=int(input("enter the no. of rows:"))
matrix=[[0]*n for _ in range(n)]
num=1

top=0
bottom=n-1
left=0
right=n-1

while top<=bottom and left<=right:
    #move top to bottom
    for i in range(top,bottom+1):
        matrix[i][left]=num
        num+=1
    left+=1
    #left to right
    for i in range(left,right+1):
        matrix[bottom][i]=num
        num+=1
    bottom-=1
    #bottom to top
    if bottom>=top: 
       for i in range(bottom,top-1,-1):
           matrix[i][right]=num
           num+=1
       right-=1
    #right to left
    if right>=left:
       for i in range(right,left-1,-1):
           matrix[top][i]=num
           num+=1
       top+=1

    
for rows in matrix:
    print(*rows)
