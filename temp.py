def solution(r, c, B, bomb):
    grid = [[1] * c for _ in range(r)]
    for b in bomb:
        b[0] -= 1
        b[1] -= 1
        grid[b[0]][b[1]] = 0
        x, y = b[0], 0
        while y < c:
            cell = x + y
            check = cell - b[2] - abs(y - b[1])
            if check < 0:
                y += 1
                continue

            if check % b[3] == 0:
                grid[x][y] = 0
            y += 1

        x, y = 0, b[1]
        while x < r:
            cell = x + y
            check = cell - b[2] - abs(x - b[0])
            if check < 0:
                x += 1
                continue

            if check % b[3] == 0:
                grid[x][y] = 0
            x += 1

    for x in range(1, r):
        grid[x][0] = grid[x][0] and grid[x - 1][0]

    for y in range(1, c):
        grid[0][y] = grid[0][y] and grid[0][y - 1]

    for x in range(1, r):
        for y in range(1, c):
            grid[x][y] = grid[x][y] and (grid[x - 1][y] or grid[x][y - 1])
			
    if grid[-1][-1]:
        return "YES\n" + str(r + c - 2)
    return "NO"

r, c, B = map(int, input().split())
bomb = []
for b in range(B):
    bomb.append(list(map(int, input().split())))
print(solution(r, c, B, bomb))
    
