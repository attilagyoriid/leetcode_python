from typing import List

from leetcode_python.src.algorithms.model.Interval import Interval


class MeetingRooms:

    def can_attend_all_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True

