import unittest

####################################################
#       Answers for the program "odd_or_pos"       #
####################################################

class program:
    def faulty_odd_or_pos(x):
        count = 0
        i = 0
        while i < len(x):
            if x[i] > 0 or x[i] % 2 == -1:
                count += 1
            i += 1
        return count

# (a) Explain what is wrong with the given code. Describe the fault precisely by proposing a modification to the code.
    def correct_odd_or_pos(x):
        count = 0
        i = 0
        while i < len(x):
            if x[i] > 0 or x[i] % 2 == 1:           # The % operation in Python returns modulus instead of remainders. Thus, if x[i] is odd, x[i] % 2 should equal 1, not -1.
                count += 1
            i += 1
        return count

# (b) If possible, give a test case that does not execute the fault. If not, briefly explain why not. (You need to give the same number of arguments.)
class test_program(unittest.TestCase):
    def test_odd_or_pos_without_executing_the_fault(self):
        x = 0                                      # Since x as type int has no len(), the program will report error before executing the fault mentioned above.
        actual = program.faulty_odd_or_pos(x)
        expected = 0
        self.assertEqual(actual, expected)

# (c) If possible, give a test case that executes the fault, but does not result in an error state. If not, briefly explain why not. (You also need to answer expected and actual output.)
    def test_odd_or_pos_executing_the_fault_without_error_state(self):
        x = [1, 4]
        actual = program.faulty_odd_or_pos(x)       # The actual out is 2.
        expected = 2                                # The expected output is 2.
        self.assertEqual(actual, expected)          # Since all elements in x are non-negative, the faulty judjement x[i] % 2 = -1 won't be executed.
                                                    # Thus, none of error state is met in this test case.

# (d) If possible, give a test case that results in an error state, but not a failure. If not, briefly explain why not. (You also need to answer expected and actual output.)
    # Without considering test case like the one given in (b), any test case that triggers an error state also results in a failure.
    # In a more detailed manner, to meet the error state, there must be some negative element x[i] in x.
    # Since x[i] % 2 equals 1, not -1, the element won't be counted, so the actual out and the expected output will differ by at least 1.

# (e) For the given test case in (d), describe the first error state. Be sure to describe the complete state.
    # There is no test case provided in (d).