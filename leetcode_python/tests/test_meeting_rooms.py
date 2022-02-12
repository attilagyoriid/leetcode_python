import unittest

from leetcode_python.src.algorithms.arrays.meeting_rooms import MeetingRooms
from leetcode_python.src.algorithms.model.Interval import Interval


class TestMeetingRooms(unittest.TestCase):

    def test_can_attend_all_meetings_failure(self):
        rooms = MeetingRooms()
        result = rooms.can_attend_all_meetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)])
        self.assertFalse(result)

    def test_can_attend_all_meetings(self):
        rooms = MeetingRooms()
        result = rooms.can_attend_all_meetings([Interval(10, 30), Interval(5, 10), Interval(30, 40)])
        self.assertTrue(result)