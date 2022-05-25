# https://www.acmicpc.net/problem/10825


try:
    import sys
    sys.stdin = open('input.txt', 'r')
except:
    pass


class PersonScore(object):
    def __init__(self, _name_person, _score_kor, _score_eng, _score_math):
        self.name_person = _name_person
        self.score_kor = _score_kor
        self.score_eng = _score_eng
        self.score_math = _score_math


if __name__ == '__main__':
    table = list()

    num_people = int(input())

    for _ in range(num_people):
        name_person, score_kor, score_eng, score_math = input().split()
        score_kor, score_eng, score_math = map(int, ( score_kor, score_eng, score_math))
        table.append((name_person, score_kor, score_eng, score_math))

    sorted_table = sorted(table, key=lambda x: (-x[1], x[2], -x[3], x[0]))
    print(sorted_table)

    for _tiem in sorted_table:
        name_person, score_kor, score_eng, score_math = _tiem
        print(name_person)
