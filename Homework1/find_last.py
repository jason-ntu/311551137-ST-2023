import unittest

###################################################
#       Answers for the program "find_last"       #
###################################################

class program:
    def faulty_find_last(x, y):
        i = len(x) - 1
        while i > 0:
            if x[i] == y:
                return i
            i -= 1
        return -1
        
# (a) Explain what is wrong with the given code. Describe the fault precisely by proposing a modification to the code.
    def correct_find_last(x, y):
        i = len(x) - 1
        while i >= 0:                           # The value of i should end with -1 instead of 0, or x[0] won't be compared.
            if x[i] == y:
                return i
            i -= 1
        return -1

# (b) If possible, give a test case that does not execute the fault. If not, briefly explain why not. (You need to give the same number of arguments.)
class test_program(unittest.TestCase):
    def test_find_last_without_executing_the_fault(self):
        x = 0                                   # Since x as type int has no len(), the program will report error before executing the fault mentioned above.
        y = 2
        actual = program.faulty_find_last(x, y)
        expected = 0
        self.assertEqual(actual, expected)

# (c) If possible, give a test case that executes the fault, but does not result in an error state. If not, briefly explain why not. (You also need to answer expected and actual output.)
    def test_find_last_executing_the_fault_without_error_state(self):
        x = []
        y = 0
        actual = program.faulty_find_last(x, y) # The actual out is -1.
        expected = -1                           # The expected output is -1.
        self.assertEqual(actual, expected)      # The fault in the while statement is executed. However, since the initial and final values of i in the correct function and the faulty function are both -1, there is no error state.
                                                    
# (d) If possible, give a test case that results in an error state, but not a failure. If not, briefly explain why not. (You also need to answer expected and actual output.)
    def test_find_last_resulting_in_error_state_without_failure(self):
        x = [2, 3, 5]
        y = 5
        actual = program.faulty_find_last(x, y) # The actual out is 2.
        expected = 2                            # The expected output is 2.
        self.assertEqual(actual, expected)      # The value of i ends with 0 rather than -1, so the error state is met.
                                                # However, the last 5 isn't located at x[0], so the error state makes no difference for the output.
                                                # That is, there is no failure in this case.

# (e) For the given test case in (d), describe the first error state. Be sure to describe the complete state.
    # The first error state is also the only error state, which has been described in (a).

