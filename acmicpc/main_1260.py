# https://www.acmicpc.net/problem/1260


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


def dfs(_maps: list, _pt_start: int) -> list:
    # print_2d_arr(_maps)
    # print(_pt_start)

    num_row, num_col = len(_maps), len(_maps[0])

    res = list()
    stack = deque()
    visited = [False] * num_col

    stack.append(_pt_start)

    while stack:
        pt_curr = stack.pop()
        if visited[pt_curr] is False:
            visited[pt_curr] = True

            # Do something.
            res.append(pt_curr)

        for _pt_new in range(len(_maps[pt_curr]) - 1, -1, -1):
            is_connected = _maps[pt_curr][_pt_new]
            if ((visited[_pt_new] is False) and (is_connected == 1)):
                stack.append(_pt_new)

    return res


def bfs(_maps: list, _pt_start: int) -> list:
    # print_2d_arr(_maps)
    # print(_pt_start)

    num_row, num_col = len(_maps), len(_maps[0])

    res = list()
    queue = deque()
    visited = [False] * num_col

    queue.append(_pt_start)

    while queue:
        pt_curr = queue.popleft()
        if visited[pt_curr] is False:
            visited[pt_curr] = True

            # Do something.
            res.append(pt_curr)

        for _pt_new, _is_connected in enumerate(_maps[pt_curr]):
            if ((visited[_pt_new] is False) and (_is_connected == 1)):
                queue.append(_pt_new)

    return res


if __name__ == '__main__':
    num_vertex, num_edge, pt_start = map(int, input().split(' '))
    maps = [[0] * num_vertex for _ in range(num_vertex)]

    for _ in range(num_edge):
        pt_pair_edge_1, pt_pair_edge_2 = map(int , input().split(' '))
        pt_pair_edge_1, pt_pair_edge_2 = pt_pair_edge_1 - 1, pt_pair_edge_2 - 1

        maps[pt_pair_edge_1][pt_pair_edge_2] = 1
        maps[pt_pair_edge_2][pt_pair_edge_1] = 1

    res_dfs = dfs(_maps=maps, _pt_start=pt_start - 1)
    res_bfs = bfs(_maps=maps, _pt_start=pt_start - 1)
    sol_dfs = ' '.join(['{}'.format(_res_dfs + 1) for _res_dfs in res_dfs])
    sol_bfs = ' '.join(['{}'.format(_res_bfs + 1) for _res_bfs in res_bfs])

    print(sol_dfs)
    print(sol_bfs)
