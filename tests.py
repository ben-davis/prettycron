import unittest

import prettycron


class CronScheduleTest(unittest.TestCase):
    def test_yearly(self):
        schedule = prettycron.CronSechdule("0 0 1 1 *")
        self.assertEqual(schedule.pretty(), "Yearly at 12:00 on 1st January")
