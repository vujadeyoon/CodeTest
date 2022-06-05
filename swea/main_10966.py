# SWEA-10966
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST&categoryId=AXWXMZta-PsDFAST&categoryType=CODE&problemTitle=10966&&&&


try:
    import sys
    sys.stdin = open('./_arxiv/sample_10966.txt', 'r')
except:
    pass


from collections import deque


def print_2d_array(_arr: list) -> None:
    num_row, num_col = len(_arr), len(_arr[0])

    for _idy in range(num_row):
        for _idx in range(num_col):
            print('{:>3}'.format(_arr[_idy][_idx]), end=' ')
        print('')


def bfs(_q, _visited):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    while _q:
        y, x = _q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= num_row or nx < 0 or nx >= num_col:
                continue

            if visited[ny][nx] != -1:
                continue

            q.append((ny, nx))
            visited[ny][nx] = visited[y][x] + 1

            print_2d_array(visited)
            print('')


if __name__=='__main__':
    for tc in range(1, int(input()) + 1):
        num_row, num_col = map(int, input().split())
        maps = [list(map(str, input())) for _ in range(num_row)]
        visited = [[-1] * num_col for _ in range(num_row)]

        q = deque()
        for i in range(num_row):
            for j in range(num_col):
                if maps[i][j]=='W':
                    q.append((i, j))
                    visited[i][j] = 0

        print('Start')
        print_2d_array(visited)
        print('')

        bfs(_q=q, _visited=visited)

        print('Result')
        print_2d_array(visited)

        result = 0
        for i in range(num_row):
            for j in range(num_col):
                result += visited[i][j]
        print("#{} {}".format(tc, result))