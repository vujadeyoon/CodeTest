"""
Dveloper: vujadeyoon
Email: vujadeyoon@gmail.com
Github: https://github.com/vujadeyoon/vujade
Title: vujade_profiler.py
Description: A module for profiler
"""


import os
import re
import traceback
import functools
import time


class DEBUG(object):
    def __init__(self):
        self.fileName = None
        self.lineNumber = None
        self.reTraceStack = re.compile('File \"(.+?)\", line (\d+?), .+')

    def get_file_line(self):
        for line in traceback.format_stack()[::-1]:
            m = re.match(self.reTraceStack, line.strip())
            if m:
                fileName = m.groups()[0]

                # ignore case
                if fileName == __file__:
                    continue
                self.fileName = os.path.split(fileName)[1]
                self.lineNumber = m.groups()[1]

                return True

        return False


def measure_time(_iter: int = 1):
    """
    Usage: @prof_.measure_time(_iter=1)
           def test(_arg):
               pass
    Description: This is a decorator which can be used to measured the elapsed time for a callable function.
    """
    if _iter < 1:
        raise ValueError('The _iter, {} should be greater than 0.'.format(_iter))

    def _measure_time(_func):
        @functools.wraps(_func)
        def _wrapper(*args, **kwargs):
            debug_info = DEBUG()
            debug_info.get_file_line()

            result = None
            time_cumsum = 0.0
            for _ in range(_iter):
                time_start = time.time()
                result = _func(*args, **kwargs)
                time_end = time.time()
                time_cumsum += (time_end - time_start)

            info_trace_1 = '[{}: {}]:'.format(debug_info.fileName, debug_info.lineNumber)
            info_trace_2 = 'The function, {} is called.'.format(_func.__name__)
            info_trace_3 = 'Total time for {} times: {:.2e} sec. Avg. time: {:.2e} sec.'.format(_iter, time_cumsum, time_cumsum / _iter)
            print('{} {} {}'.format(info_trace_1, info_trace_2, info_trace_3))
            return result
        return _wrapper
    return _measure_time


class TimeProfiler(DEBUG):
    def __init__(self) -> None:
        DEBUG.__init__(self)
        self.cnt_call = 0
        self.time_start = 0.0
        self.time_prev = 0.0
        self.time_curr = 0.0
        self.elapsed_time_total = 0.0
        self.elapsed_time_prev = 0.0
        self.elapsed_time_curr = 0.0

    def run(self, _is_print: bool = False, _is_pause: bool = False) -> None:
        if self.cnt_call != 0:
            if _is_pause is True:
                _print = input
            else:
                _print = print

            self.get_file_line()
            self._update()

            info_mem = 'Total time: {:.2f} sec., Time: {:.2f} sec.'.format(self.elapsed_time_total, self.elapsed_time_curr)
            info_trace = '[{}: {}] '.format(self.fileName, self.lineNumber) + info_mem
            _print(info_trace)
        else:
            self.time_start = time.time()
            self.time_prev = self.time_start

        self.cnt_call += 1

    def _update(self):
        self.time_curr = time.time()
        self.elapsed_time_total = self._get_elapsed_time_total()
        self.elapsed_time_curr = self._get_elapsed_time()

        self.time_prev = self.time_curr
        self.elapsed_time_prev = self.elapsed_time_curr

    def _get_elapsed_time(self):
        return self.time_curr - self.time_prev

    def _get_elapsed_time_total(self):
        return self.time_curr - self.time_start


class AverageMeterTime(object):
    """This class is intended to profile the processing time"""
    def __init__(self, _warmup: int = 0):
        """
        :param int _warmup: A number of times for warming up.
        """
        self.warmup = _warmup
        self.cnt_call = 0
        self.time_len = 0
        self.time_sum = 0.0
        self.time_avg = 0.0
        self.fps_avg = 0.0
        self.eps_val = 1e-9

    def tic(self):
        self.time_start = time.time()

    def toc(self):
        self.time_end = time.time()
        self.cnt_call += 1

        if self.warmup < self.cnt_call:
            self._update()

    def _update(self):
        self.time_len = (self.cnt_call - self.warmup)
        self.time_sum += (self.time_end - self.time_start)
        self.time_avg = (self.time_sum / self.time_len)
        self.fps_avg = 1 / (self.time_avg + self.eps_val)
