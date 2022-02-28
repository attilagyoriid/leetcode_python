from typing import List


class InsertInterval:
    def insert(self, intervals: List[List[int]], interval_to_insert: List[int]) -> List[List[int]]:

        new_intervals = []

        for i in range(len(intervals)):
            if interval_to_insert[1] < intervals[i][0]:
                new_intervals.append(interval_to_insert)
                return new_intervals + intervals[i:]
            elif interval_to_insert[0] > intervals[i][1]:
                new_intervals.append(intervals[i])
            else:
                interval_to_insert = [min(interval_to_insert[0], intervals[i][0]),
                                      max(interval_to_insert[1], intervals[i][1])]

        new_intervals.append(interval_to_insert)
        return new_intervals
