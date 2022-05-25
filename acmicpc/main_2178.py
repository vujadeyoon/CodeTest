# https://www.acmicpc.net/problem/2178


try:
    import sys
    sys.stdin = open('input.txt', 'r')
except:
    pass


from collections import deque


def print_2d_arr(_arr: list):
    num_row, num_col = len(_arr), len(_arr[0])

    for _idy in range(num_row):
        for _idx in range(num_col):
            print('{:>3}'.format(_arr[_idy][_idx]), end=' ')
        print('')


def is_out_of_range(_y, _x, _num_row, _num_col):
    return (_y < 0) or (_num_row <= _y) or (_x < 0) or (_num_col <= _x)


def sol_bfs(_arr: list):
    # print_2d_arr(arr)

    num_row, num_col = len(_arr), len(_arr[0])
    visited = [[0] * num_col for _ in range(num_row)]
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    queue = deque()

    visited[0][0] = 1
    queue.append((0, 0))

    while queue:
        idy_curr, idx_curr = queue.popleft()
        # print('({}, {})'.format(idy_curr, idx_curr))
        for _dy, _dx in zip(dy, dx):
            idy_new = idy_curr + _dy
            idx_new = idx_curr + _dx

            if visited[idy_new][idx_new] is False:
                visited[idy_new][idx_new] = visited[idy_curr][idx_curr] + 1

            if (is_out_of_range(idy_new, idx_new, num_row, num_col) is False):
                if ((visited[idy_new][idx_new] == 0) and (_arr[idy_new][idx_new] == 1)):
                    queue.append((idy_new, idx_new))

    # print_2d_arr(visited)

    return visited[-1][-1]


if __name__ == '__main__':
    num_row, num_col = map(int, input().split(' '))
    arr = [list(map(int, input())) for _ in range(num_row)]
    res = sol_bfs(arr)
    print(res)
