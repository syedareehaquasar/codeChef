n,m,k=map(int,input().split())
visited=[[1 for i in range(m)] for j in range(n)]
for _ in range(k):
    a,b,t,f=map(int,input().split())
    visited[a-1][b-1]=0
    a-=1
    b-=1
    y=b
    
    for i in range(n):
        l=y+i-t-abs((a-i))
        if l>=0 and not l%f:
                visited[i][y]=0
    x=a
    for i in range(m):
        l=x+i-t-abs(b-i)
        if l>=0 and not l%f:
            visited[x][i]=0

for i in range(1,m):
    visited[0][i]=visited[0][i-1] and visited[0][i]
for i in range(1,n):
    visited[i][0]=visited[i-1][0] and visited[i][0]
for i in range(1,n):
    for j in range(1,m):
        if visited[i][j]==0:
            continue
        visited[i][j]=visited[i-1][j] or visited[i][j-1]
if visited[-1][-1]:
    print("YES")
    print(n+m-2)
else:
    print("NO")
    
