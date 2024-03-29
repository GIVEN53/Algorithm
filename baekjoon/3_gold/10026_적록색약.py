from sys import stdin, setrecursionlimit
from collections import deque


# 1
def dfs(x, y, color_weakness):
    global rg_visited, rgb_visited

    for i in range(4):
        nx = x + direction[i]
        ny = y + direction[3 - i]
        if is_out_of_range(nx, ny):
            continue

        if color_weakness:
            if rg_visited[nx][ny]:
                continue

            if board[x][y] in {'R', 'G'} and board[nx][ny] in {'R', 'G'}:
                rg_visited[nx][ny] = True
                dfs(nx, ny, color_weakness)
            elif board[x][y] == board[nx][ny]:
                rg_visited[nx][ny] = True
                dfs(nx, ny, color_weakness)
        else:
            if rgb_visited[nx][ny]:
                continue

            if board[x][y] == board[nx][ny]:
                rgb_visited[nx][ny] = True
                dfs(nx, ny, color_weakness)


def is_out_of_range(x, y):
    return x < 0 or x > n - 1 or y < 0 or y > n - 1


setrecursionlimit(10**4)
n = int(stdin.readline())
board = [list(stdin.readline().rstrip()) for _ in range(n)]

rg_visited = [[False] * n for _ in range(n)]
rgb_visited = [[False] * n for _ in range(n)]
direction = [0, 0, 1, -1]
rg_count, rgb_count = 0, 0

for i in range(n):
    for j in range(n):
        if not rg_visited[i][j]:
            rg_count += 1
            dfs(i, j, True)
        if not rgb_visited[i][j]:
            rgb_count += 1
            dfs(i, j, False)

print(rgb_count, rg_count)


# 2
def bfs(diff_color):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            count += 1
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + direction[k]
                    ny = y + direction[3 - k]

                    if is_out_of_range(nx, ny) or visited[nx][ny] or board[nx][ny] in diff_color[board[i][j]]:
                        continue

                    visited[nx][ny] = True
                    q.append((nx, ny))
    return count


def is_out_of_range(x, y):
    return x < 0 or x > n - 1 or y < 0 or y > n - 1


n = int(stdin.readline())
board = [list(stdin.readline().rstrip()) for _ in range(n)]

diff_color_rgb = {'R': {'G', 'B'}, 'G': {'R', 'B'}, 'B': {'R', 'G'}}
diff_color_rg = {'R': {'B'}, 'G': {'B'}, 'B': {'R', 'G'}}
direction = [0, 0, 1, -1]

print(bfs(diff_color_rgb), bfs(diff_color_rg))
