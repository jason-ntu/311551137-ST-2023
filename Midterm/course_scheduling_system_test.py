import unittest
from unittest.mock import patch
from unittest.mock import Mock
from course_scheduling_system import CSS


class CSSTest(unittest.TestCase):

    def setUp(self):
        self.css = CSS()

    # Let check_course_exist return True by mocking(Stub).
    @patch.object(CSS, "check_course_exist", return_value=True)
    def test_q1_1(self, mock_check_course_exist):

        # Try to add one course by add_course, check its return value
        course = ('Algorithms', 'Monday', 3, 4)
        self.assertTrue(self.css.add_course(course))

        # Verify the result by get_course_list.
        course_list = self.css.get_course_list()
        self.assertEqual(len(course_list), 1)

    # Let check_course_exist return True by mocking.
    @patch.object(CSS, "check_course_exist", return_value=True)
    def test_q1_2(self, mock_check_course_exist):
        # Try to add two courses overlapping with each other, check its return value
        course = ('Algorithms', 'Monday', 3, 4)
        overlapping_course = ('Algorithms', 'Monday', 4, 5)
        self.assertTrue(self.css.add_course(course))
        self.assertFalse(self.css.add_course(overlapping_course))

        # Verify the result.
        course_list = self.css.get_course_list()
        self.assertEqual(len(course_list), 1)
        self.assertEqual(course_list[0], course)

    # Let check_course_exist return False by mocking.
    @patch.object(CSS, "check_course_exist", return_value=False)
    def test_q1_3(self, mock_check_course_exist):
        # Try to add one course, and Check its return value.
        course = ('Algorithms', 'Monday', 3, 4)
        self.assertFalse(self.css.add_course(course))

    # Let check_course_exist return True by mocking.
    @patch.object(CSS, "check_course_exist", return_value=True)
    def test_q1_4(self, mock_check_course_exist):
        # Try to add a invalid course input, and check the Exception raised.
        invalid_course_len_3 = ('Algorithms', 'Monday', 3)
        invalid_course_first_not_str = (3, 4, 'Algorithms', 'Monday')
        invalid_course_not_in_workdays = ('Algorithms', 'Sunday', 3, 4)
        invalid_course_reversed_time = ('Algorithms', 'Monday', 4, 3)
        courses = [invalid_course_len_3,
                   invalid_course_first_not_str,
                   invalid_course_not_in_workdays,
                   invalid_course_reversed_time]
        for course in courses:
            with self.subTest():
                with self.assertRaisesRegex(TypeError, ''):
                    self.css.add_course(course)

    # Let check_course_exist return True by mocking.
    @patch.object(CSS, "check_course_exist", return_value=True)
    def test_q1_5(self, mock_check_course_exist):
        # Add three courses that don’t overlapp with each other
        course_on_mon = ('Algorithms', 'Monday', 3, 4)
        course_on_tues = ('Algorithms', 'Tuesday', 3, 4)
        course_on_wed = ('Algorithms', 'Wednesday', 3, 4)
        self.assertTrue(self.css.add_course(course_on_mon))
        self.assertTrue(self.css.add_course(course_on_tues))
        self.assertTrue(self.css.add_course(course_on_wed))

        # Remove the second one by remove_course
        self.assertTrue(self.css.remove_course(course_on_tues))

        # Verify the result
        course_list = self.css.get_course_list()
        self.assertEqual(len(course_list), 2)
        self.assertEqual(course_list[0], course_on_mon)
        self.assertEqual(course_list[1], course_on_wed)

        # Check the call count of check_course_exist
        self.assertEqual(mock_check_course_exist.call_count, 4)

        # Print out the schedule in a formatted way.
        print(self.css)

    # Add some more(possibly 0) tests to achieve 100 % coverage of
    # course_scheduling_system.py. You can mock check_course_exist
    # and use pragma to excluding check_course_exist from coverage analysis.
    @patch.object(CSS, "check_course_exist", return_value=False)
    def test_q1_6_1(self, mock_check_course_exist):
        # line 56
        course = ('Algorithms', 'Monday', 3, 4)
        self.assertFalse(self.css.remove_course(course))

    @patch.object(CSS, "check_course_exist", return_value=True)
    def test_q1_6_2(self, mock_check_course_exist):
        # line 58
        course = ('Algorithms', 'Monday', 3, 4)
        self.assertFalse(self.css.remove_course(course))


if __name__ == "__main__":  # pragma no cover
    unittest.main()
