import collections
import re
from operator import itemgetter
from typing import List
from vujade import vujade_profiler as prof_
from vujade.vujade_debug import printf


class Solution_1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        res = list()
        list_char = list()
        list_id_char = list()
        list_id_num = list()
        set_index = set()

        for _idx, _log in enumerate(logs):
            # printf(type(_log), _log)
            identifier = _log[:_log.find(' ')]
            remains = _log[_log.find(' ')+1:]
            if remains[0].isalpha() is True:
                list_id_char.append(_log)
                list_char.append(remains)
            else:
                list_id_num.append(_log)

        indices, sorted_list_char = zip(*sorted(enumerate(list_char), key=itemgetter(1)))

        printf(logs)
        printf(list_char)
        printf(list_id_char)
        printf(list_id_num)
        printf(indices)
        printf(sorted_list_char)
        counter = collections.Counter(sorted_list_char)

        if len(sorted_list_char) != len(set(sorted_list_char)):
            for k, v in counter.items():
                temp = list()
                if 1 < v:
                    index_duplicated = [i for i, x in enumerate(list_char) if x == k]
                    printf(index_duplicated)
                    for _index_dup in index_duplicated:
                        printf(_index_dup)
                        temp.append(list_id_char[_index_dup])
                    indices_temp, sorted_temp = zip(*sorted(enumerate(temp), key=itemgetter(1)))

                    for _idx_temp in indices_temp:
                        indices
                        index_duplicated[_idx_temp]

                    printf(indices_temp)
                    printf(sorted_temp)





        for _idx, _index in enumerate(indices):
            # index = list_char.index(_ele)
            #
            # if index in set_index:
            #     printf(index)

            res.append(list_id_char[_index])
            # set_index.add(_index)

        res.extend(list_id_num)

        return res


if __name__=='__main__':
    avgmeter_time = prof_.AverageMeterTime(_warmup=0)

    # case_1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    # Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    # case_2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    # Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    case_3 = ["dig1 8 1 5 1","let5 art can","dig2 3 6","let2 own kit dig","let3 art can"]

    sol = Solution_1()

    avgmeter_time.tic()
    # printf(sol.reorderLogFiles(logs=case_1), _is_pause=False)
    # printf(sol.reorderLogFiles(logs=case_2), _is_pause=False)
    printf(sol.reorderLogFiles(logs=case_3), _is_pause=False)
    avgmeter_time.toc()

    printf(f"Averaged elapsed time: {avgmeter_time.time_avg:.2e}", _is_pause=False)
