import unittest
import Students
from contextlib import redirect_stdout
import io

buf = io.StringIO()


class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary', 'Thomas', 'Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        with redirect_stdout(buf):
            print('Start set_name test\n')
            for name in self.user_name:
                self.user_id.append(self.students.set_name(name))
                print(self.user_id[-1], name)
                self.assertNotIn(self.user_id[-1], self.user_id[:-1])
            self.assertEqual(len(self.user_name), len(self.user_id))
            print('\nFinish set_name test\n')

    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        with redirect_stdout(buf):
            print('Start get_name test\n\nuser_id length = %d\nuser_name length = %d\n' %
                  (len(self.user_id), len(self.user_name)))
            self.assertEqual(len(self.user_name), len(self.user_id))
            for i, id in enumerate(self.user_id):
                print('id', id, ':', self.students.get_name(id))
                self.assertEqual(self.students.get_name(id), self.user_name[i])
            mex = 0
            while (mex in self.user_id):
                mex += 1
            self.assertEqual(self.students.get_name(mex),
                             'There is no such user')
            print('\nFinish get_name test')


if __name__ == '__main__':  # pragma: no cover
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    print(buf.getvalue())
