from typing import List


class RemoveCoveredIntervals:

    def get_intervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))

        resultIntervals = [intervals[0]]

        for current_left, current_right in intervals[1:]:
            previous_left, previous_right = resultIntervals[-1]
            if previous_left <= current_left and previous_right >= current_right:
                continue

            resultIntervals.append([current_left, current_right])

        return len(resultIntervals)
