import unittest

###################################################
#       Answers for the program "last_zero"       #
###################################################

class program:
    def faulty_last_zero(x):
        i = 0
        while i < len(x):
            if x[i] == 0:
                return i
            i += 1
        return -1
        
# (a) Explain what is wrong with the given code. Describe the fault precisely by proposing a modification to the code.
    def correct_last_zero(x):                   # Followings are the error states:
        i = len(x) - 1                          # The initial value should be len(x) - 1, not 0.
        while i >= 0:                           # The iteration should end with -1, not len(x).
            if x[i] == 0:
                return i
            i -= 1                              # The value of i should be decreased rather than being increased.
        return -1

# (b) If possible, give a test case that does not execute the fault. If not, briefly explain why not. (You need to give the same number of arguments.)
    # This is impossible since the first error state is at the first line of the function, and any input must execute the first line.

# (c) If possible, give a test case that executes the fault, but does not result in an error state. If not, briefly explain why not. (You also need to answer expected and actual output.)
class test_program(unittest.TestCase):
    def test_last_zero_executing_the_fault_without_error_state(self):
        x = [0]
        actual = program.faulty_last_zero(x)    # The actual out is 0.
        expected = 0                            # The expected output is 0.
        self.assertEqual(actual, expected)      # Since len(x) - 1 = 0, the error state in the initialization phase won't make any difference.
                                                # Besides, the input x[0] = 0 makes the loop end before i is decreased/increased for the first time.
                                                # Thus, none of error state is met in this test case.

# (d) If possible, give a test case that results in an error state, but not a failure. If not, briefly explain why not. (You also need to answer expected and actual output.)
    def test_last_zero_resulting_in_error_state_without_failure(self):
        x = [0, 1, 2]
        actual = program.faulty_last_zero(x)    # The actual out is 0.
        expected = 0                            # The expected output is 0.
        self.assertEqual(actual, expected)      # The fault is executed, so there is an error state, but there is no failure.

# (e) For the given test case in (d), describe the first error state. Be sure to describe the complete state.
    # The first error state is at the first line of the function, where i should be initialized to len(x) - 1 = 2, but instead is initialized to 0.