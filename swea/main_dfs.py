try:
    import sys
    sys.stdin = open('./_arxiv/sample_dfs_bfs.txt', 'r')
except:
    pass


from collections import deque


def print_2d_array(_arr: list) -> None:
    num_row, num_col = len(_arr), len(_arr[0])

    for _idy in range(num_row):
        for _idx in range(num_col):
            print('{:>3}'.format(_arr[_idy][_idx]), end=' ')
        print('')


def is_out_of_range(_idy: int, _idx: int, _num_row: int, _num_col: int) -> bool:
    return (_idy < 0) or (_num_row <= _idy) or (_idx < 0) or (_num_col <= _idx)


def dfs(_maps: list, _idy: int, _idx: int):
    num_row, num_col = len(_maps), len(_maps[0])

    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]

    _maps[_idy][_idx] = 'S'

    for _dy, _dx in zip(dy, dx):
        idy_new = _idy + _dy
        idx_new = _idx + _dx

        if is_out_of_range(_idy=idy_new, _idx=idx_new, _num_row=num_row, _num_col=num_col) is True:
            continue
        else:
            if _maps[idy_new][idx_new] == 'L':
                dfs(_maps=_maps, _idy=idy_new, _idx=idx_new)


if __name__=='__main__':
    q = deque()

    num_test = int(input())

    for _num_test in range(1, num_test + 1):
        q.clear()
        num_row, num_col = map(int, input().split())
        maps = [list(map(str, input())) for _ in range(num_row)]

        for _idy in range(num_row):
            for _idx in range(num_col):
                if maps[_idy][_idx] == 'L':
                    q.append((_idy, _idx))

        while q:
            idy, idx = q.popleft()
            if maps[idy][idx] == 'L':
                dfs(_maps=maps, _idy=idy, _idx=idx)

        print_2d_array(maps)
