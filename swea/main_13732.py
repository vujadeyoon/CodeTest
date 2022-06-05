# SWEA-13732
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AX8BAN1qTwoDFARO


# try:
#     import sys
#     sys.stdin = open('./_arxiv/sample_13732.txt', 'r')
# except:
#     pass


def print_2d_array(_arr: list) -> None:
    num_row, num_col = len(_arr), len(_arr[0])

    for _idy in range(num_row):
        for _idx in range(num_col):
            print('{:>3}'.format(_arr[_idy][_idx]), end=' ')
        print('')


def char2int(_char: str) -> int:
    if _char == '#':
        # SWEA-13732
        # https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AX8BAN1qTwoDFARO

        # try:
        #     import sys
        #     sys.stdin = open('./_arxiv/sample_13732.txt', 'r')
        # except:
        #     pass

        def print_2d_array(_arr: list) -> None:
            num_row, num_col = len(_arr), len(_arr[0])

            for _idy in range(num_row):
                for _idx in range(num_col):
                    print('{:>3}'.format(_arr[_idy][_idx]), end=' ')
                print('')

        def char2int(_char: str) -> int:
            if _char == '#':
                res = 1
            else:
                res = 0

            return res

        def get_start_pos_rectangle_candidate(_arr: list) -> tuple:
            num_row, num_col = len(_arr), len(_arr[0])
            res_y = 0
            res_x = 0

            is_break = False
            for _idy in range(num_row):
                for _idx in range(num_col):
                    if _arr[_idy][_idx] == '#':
                        res_y = _idy
                        res_x = _idx
                        is_break = True
                        break

                if is_break is True:
                    break

            return res_y, res_x

        def get_horizontal_len_rec(_arr: list, _idy: int, _idx_start: int, _num_col: int) -> int:
            res = 0
            is_connected = True
            is_can_be_connected = True

            if _arr[_idy][_idx_start] == '.':
                is_connected = False
            else:
                for _idx in range(_idx_start, _num_col):
                    if is_can_be_connected is True:
                        if _arr[_idy][_idx] == '#':
                            res += 1
                        else:  # elif _arr[_idy][_idx] == '.':
                            is_can_be_connected = False
                    else:
                        if _arr[_idy][_idx] == '#':
                            is_connected = False
                            break

            if is_connected is False:
                res = 0

            return res

        def get_vertical_len_rec(_arr: list, _idx: int, _idy_start: int, _num_row: int) -> int:
            res = 0
            is_connected = True
            is_can_be_connected = True

            if _arr[_idy_start][_idx] == '.':
                is_connected = False
            else:
                for _idy in range(_idy_start, _num_row):
                    if is_can_be_connected is True:
                        if _arr[_idy][_idx] == '#':
                            res += 1
                        else:  # elif _arr[_idy][_idx] == '.':
                            is_can_be_connected = False
                    else:
                        if _arr[_idy][_idx] == '#':
                            is_connected = False
                            break

            if is_connected is False:
                res = 0

            return res

        def sol_1(_arr: list, _pos_start: tuple) -> str:
            # print_2d_array(_arr)
            # print(_pos_start)

            res = 'yes'
            num_row, num_col = len(_arr), len(_arr[0])
            idy_start = _pos_start[0]
            idx_start = _pos_start[1]

            horizontal_len_rec_candidate = get_horizontal_len_rec(_arr=_arr, _idy=idy_start, _idx_start=idx_start,
                                                                  _num_col=num_col)

            if horizontal_len_rec_candidate == 0:
                res = 'no'
            else:
                for _idy in range(idy_start, num_row):
                    max_idy = idy_start + horizontal_len_rec_candidate - 1

                    if (idy_start <= _idy) and (_idy <= max_idy):
                        horizontal_len_rec_curr = get_horizontal_len_rec(_arr=_arr, _idy=_idy, _idx_start=idx_start,
                                                                         _num_col=num_col)
                        if horizontal_len_rec_curr != horizontal_len_rec_candidate:
                            res = 'no'
                            break

                    if ((idy_start + horizontal_len_rec_candidate - 1) < _idy) and (_arr[_idy][idx_start] == '#'):
                        res = 'no'
                        break

            return res

        def sol_2(_arr: list, _pos_start: tuple, _is_debug: bool = False) -> str:
            # print_2d_array(_arr)
            # print(_pos_start)

            res = 'yes'
            num_row, num_col = len(_arr), len(_arr[0])
            idy_start = _pos_start[0]
            idx_start = _pos_start[1]

            len_hori = 0
            for _cnt, _n in enumerate(range(idy_start, num_row)):
                len_hori_candidate = get_horizontal_len_rec(_arr=_arr, _idy=_n, _idx_start=_n, _num_col=num_col)
                len_verti_candidate = get_horizontal_len_rec(_arr=_arr, _idy=_n, _idx_start=_n, _num_col=num_col)

                if (_is_debug is True):
                    print('len_hori_candidate: ', len_hori_candidate)
                    print('len_verti_candidate: ', len_verti_candidate)

                if _cnt == 0:
                    len_hori = len_hori_candidate

                if (_is_debug is True):
                    print('len_hori: ', len_hori)
                    print('_cnt: ', _cnt)
                    print('_n: ', _n)
                    print('len_hori - _n: ', len_hori - _n)

                if _cnt < len_hori:
                    if ((len_hori_candidate == (len_hori - _cnt)) and (
                            len_hori_candidate == len_verti_candidate)) is False:
                        res = 'no'
                        break

                    if len_hori == 0:
                        res = 'no'
                else:
                    if (len_hori_candidate != 0) or (len_verti_candidate != 0):
                        res = 'no'

            return res

        def check(board, cnt, n):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        down = 0
                        right = 0
                        for k in range(i + 1, n):
                            if board[k][j] == 1:
                                down += 1
                            else:
                                break

                        for k in range(j + 1, n):
                            if board[i][k] == 1:
                                right += 1
                            else:
                                break

                        if down != right:
                            return 'no'

                        for x in range(i, i + down + 1):
                            for y in range(j, j + right + 1):
                                if board[x][y] == 1:
                                    cnt -= 1
                                else:
                                    return 'no'

                        if cnt != 0:
                            return 'no'
                        return 'yes'

        if __name__ == '__main__':
            T = int(input())

            for _num_test in range(1, T + 1):
                len_rectangle = int(input())
                board = [list(input()) for _ in range(len_rectangle)]
                idy, idx = get_start_pos_rectangle_candidate(_arr=board)

                res = sol_2(_arr=board, _pos_start=(idy, idx))

                print('#{} {}'.format(_num_test, res))

                # board = [list(map(char2int, input())) for _ in range(len_rectangle)]
                # result = check(board, cnt, n)

                # print_2d_array(board)
    else:
        res = 0

    return res


def get_start_pos_rectangle_candidate(_arr: list) -> tuple:
    num_row, num_col = len(_arr), len(_arr[0])
    res_y = 0
    res_x = 0

    is_break = False
    for _idy in range(num_row):
        for _idx in range(num_col):
            if _arr[_idy][_idx] == '#':
                res_y = _idy
                res_x = _idx
                is_break = True
                break

        if is_break is True:
            break

    return res_y, res_x


def get_horizontal_len_rec(_arr: list, _idy: int, _idx_start:int, _num_col: int) -> int:
    res = 0
    is_connected = True
    is_can_be_connected = True

    if _arr[_idy][_idx_start] == '.':
        is_connected = False
    else:
        for _idx in range(_idx_start, _num_col):
            if is_can_be_connected is True:
                if _arr[_idy][_idx] == '#':
                    res += 1
                else: # elif _arr[_idy][_idx] == '.':
                    is_can_be_connected = False
            else:
                if _arr[_idy][_idx] == '#':
                    is_connected = False
                    break

    if is_connected is False:
        res = 0

    return res


def get_vertical_len_rec(_arr: list, _idx: int, _idy_start:int, _num_row: int) -> int:
    res = 0
    is_connected = True
    is_can_be_connected = True

    if _arr[_idy_start][_idx] == '.':
        is_connected = False
    else:
        for _idy in range(_idy_start, _num_row):
            if is_can_be_connected is True:
                if _arr[_idy][_idx] == '#':
                    res += 1
                else: # elif _arr[_idy][_idx] == '.':
                    is_can_be_connected = False
            else:
                if _arr[_idy][_idx] == '#':
                    is_connected = False
                    break

    if is_connected is False:
        res = 0

    return res


def sol_1(_arr: list, _pos_start: tuple) -> str:
    # _2d_array(_arr)
    # print(_pos_start)

    res = 'yes'
    num_row, num_col = len(_arr), len(_arr[0])
    idy_start = _pos_start[0]
    idx_start = _pos_start[1]

    horizontal_len_rec_candidate = get_horizontal_len_rec(_arr=_arr, _idy=idy_start, _idx_start=idx_start, _num_col=num_col)

    if horizontal_len_rec_candidate == 0:
        res = 'no'
    else:
        for _idy in range(idy_start, num_row):
            max_idy = idy_start + horizontal_len_rec_candidate - 1

            if (idy_start <= _idy) and (_idy <= max_idy):
                horizontal_len_rec_curr = get_horizontal_len_rec(_arr=_arr, _idy=_idy, _idx_start=idx_start, _num_col=num_col)
                if horizontal_len_rec_curr != horizontal_len_rec_candidate:
                    res = 'no'
                    break

            if ((idy_start + horizontal_len_rec_candidate - 1) < _idy) and (_arr[_idy][idx_start] == '#'):
                res = 'no'
                break

    return res


def sol_2(_arr: list, _pos_start: tuple, _is_debug: bool = False) -> str:
    # print_2d_array(_arr)
    # print(_pos_start)

    res = 'yes'
    num_row, num_col = len(_arr), len(_arr[0])
    idy_start = _pos_start[0]
    idx_start = _pos_start[1]

    len_hori = 0
    for _cnt, _n in enumerate(range(idy_start, num_row)):
        len_hori_candidate = get_horizontal_len_rec(_arr=_arr, _idy=_n, _idx_start=_n, _num_col=num_col)
        len_verti_candidate = get_horizontal_len_rec(_arr=_arr, _idy=_n, _idx_start=_n, _num_col=num_col)

        if (_is_debug is True):
            print('len_hori_candidate: ', len_hori_candidate)
            print('len_verti_candidate: ', len_verti_candidate)

        if _cnt == 0:
            len_hori = len_hori_candidate

        if (_is_debug is True):
            print('len_hori: ', len_hori)
            print('_cnt: ', _cnt)
            print('_n: ', _n)
            print('len_hori - _n: ', len_hori - _n)

        if _cnt < len_hori:
            if ((len_hori_candidate == (len_hori - _cnt)) and (len_hori_candidate == len_verti_candidate)) is False:
                res = 'no'
                break

            if len_hori == 0:
                res = 'no'
        else:
            if (len_hori_candidate != 0) or (len_verti_candidate !=0):
                res = 'no'

    return res




def check(board, cnt, n) :
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                down = 0
                right = 0
                for k in range(i+1, n) :
                    if board[k][j] == 1 :
                        down +=1
                    else :
                        break

                for k in range(j+1, n) :
                    if board[i][k] == 1 :
                        right += 1
                    else :
                        break

                if down != right :
                    return 'no'

                for x in range(i, i+down + 1) :
                    for y in range(j, j+right + 1) :
                        if board[x][y] == 1 :
                            cnt -= 1
                        else :
                            return 'no'

                if cnt != 0 :
                    return 'no'
                return 'yes'


if __name__=='__main__':
    T = int(input())

    for _num_test in range(1, T+1):
        len_rectangle = int(input())
        board = [list(input()) for _ in range(len_rectangle)]
        idy, idx = get_start_pos_rectangle_candidate(_arr=board)

        res = sol_2(_arr=board, _pos_start=(idy, idx))

        print('#{} {}'.format(_num_test, res))

        # board = [list(map(char2int, input())) for _ in range(len_rectangle)]
        # result = check(board, cnt, n)

        # print_2d_array(board)
