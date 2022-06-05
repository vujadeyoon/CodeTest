import collections
import re
from typing import List
from vujade import vujade_profiler as prof_
from vujade.vujade_debug import printf


class Solution_1:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for _idx in range(int(len_s / 2)):
            s[_idx], s[-1 - _idx] = s[-1 - _idx], s[_idx]


class Solution_2:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


class Solution_3:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


class Solution_4:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

if __name__=='__main__':
    avgmeter_time = prof_.AverageMeterTime(_warmup=0)

    case_1 = ["h", "e", "l", "l", "o"]
    case_2 = ["H", "a", "n", "n", "a", "h"]

    sol = Solution_3()

    avgmeter_time.tic()
    sol.reverseString(s=case_1)
    sol.reverseString(s=case_2)
    avgmeter_time.toc()

    printf(case_1, _is_pause=False)
    printf(case_2, _is_pause=False)
    printf(f"Averaged elapsed time: {avgmeter_time.time_avg:.2e}", _is_pause=False)
