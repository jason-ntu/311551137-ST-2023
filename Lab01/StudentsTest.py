import unittest
import Students
import sys
import io


class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary', 'Thomas', 'Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        print('Start set_name test\n')
        for name in self.user_name:
            curId = self.students.set_name(name)
            print(curId, name)
            self.assertNotIn(curId, self.user_id)
            self.user_id.append(curId)
        self.assertEqual(len(self.user_name), len(self.user_id))
        print('\nFinish set_name test\n')
        pass

    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        print('Start get_name test\n')
        print('user_id length = ', len(self.user_id))
        print('user_name length = ', len(self.user_name), '\n')
        self.assertEqual(len(self.user_name), len(self.user_id))
        mex = 0
        while (mex in self.user_id):
            mex += 1
        self.user_id.append(mex)
        self.user_name.append('There is no such user')
        for i in range(len(self.user_id)):
            name = self.students.get_name(self.user_id[i])
            print('id', self.user_id[i], ':', name)
            self.assertEqual(name, self.user_name[i])
        self.user_id.pop()
        self.user_name.pop()
        print('\nFinish get_name test')
        pass


# if __name__ == '__main__':
#     # Create a test suite from your tests
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test)

#     # Create a TextTestRunner and redirect the output to the console
#     # runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
#     runner = unittest.TextTestRunner(stream=sys.stdout, buffer=True)

#     # Run the test suite and capture the result
#     result = runner.run(suite)

#     # Print the contents of the buffer
#     print(result.buffer.getvalue())


# if __name__ == '__main__':
#     # Create a test suite from your tests
#     suite = unittest.TestLoader().loadTestsFromTestCase(Test)

#     # Create an in-memory buffer
#     buffer = io.StringIO()

#     # Create a TextTestRunner and redirect the output to the buffer
#     runner = unittest.TextTestRunner(stream=buffer)

#     # Run the test suite
#     result = runner.run(suite)

#     # Print the contents of the buffer
#     print(buffer.getvalue())
