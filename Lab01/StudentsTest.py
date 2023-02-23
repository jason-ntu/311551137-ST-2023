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
