from typing import List


class NonOverlappingIntervals:
    def calculate(self, intervals: List[List[int]]) -> int:
        deleted_intervals = 0
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= previous_end:
                previous_end = end
            else:
                deleted_intervals += 1
                previous_end = min(previous_end, end)

        return deleted_intervals

