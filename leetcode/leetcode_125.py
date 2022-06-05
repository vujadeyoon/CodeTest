import collections
import re
from vujade import vujade_profiler as prof_
from vujade.vujade_debug import printf


class Solution_1:
    def isPalindrome(self, s: str) -> bool:
        list_alnum = list()
        for _idx, _s in enumerate(s):
            if _s.isalnum() is True:
                list_alnum.append(_s.lower())

        list_alnum_reversed = list_alnum[::-1]

        if list_alnum == list_alnum_reversed:
            res = True
        else:
            res = False

        return res


class Solution_2:
    def isPalindrome(self, s: str) -> bool:
        res = True

        list_alnum = list()
        for _idx, _s in enumerate(s):
            if _s.isalnum() is True:
                list_alnum.append(_s.lower())

        while (1 < len(list_alnum)):
            if list_alnum.pop() != list_alnum.pop(0):
                res = False
                break

        return res


class Solution_3:
    def isPalindrome(self, s: str) -> bool:
        res = True

        deque_alnum = collections.deque()
        for _idx, _s in enumerate(s):
            if _s.isalnum() is True:
                deque_alnum.append(_s.lower())

        while (1 < len(deque_alnum)):
            if deque_alnum.pop() != deque_alnum.popleft():
                res = False
                break

        return res


class Solution_4:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


if __name__=='__main__':
    avgmeter_time = prof_.AverageMeterTime(_warmup=0)

    case_1 = "A man, a plan, a canal: Panama"
    case_2 = "race a car"
    case_3 = " "

    sol = Solution_4()

    avgmeter_time.tic()
    printf(sol.isPalindrome(s=case_1), _is_pause=False)
    printf(sol.isPalindrome(s=case_2), _is_pause=False)
    printf(sol.isPalindrome(s=case_3), _is_pause=False)
    avgmeter_time.toc()

    printf(f"Averaged elapsed time: {avgmeter_time.time_avg:.2e}", _is_pause=False)
