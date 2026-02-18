from bisect import bisect_left, bisect_right


class ExamTracker:

    def __init__(self):
        self.time_list = []
        self.pre_sum = [0]

    def record(self, time: int, score: int) -> None:
        self.time_list.append(time)
        self.pre_sum.append(self.pre_sum[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        l = bisect_left(self.time_list, startTime)
        r = bisect_right(self.time_list, endTime)
        return self.pre_sum[r] - self.pre_sum[l]
