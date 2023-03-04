import unittest
from unittest.mock import patch
from app import Application, MailSystem


class ApplicationStub():
    def __init__(self, people=[], selected=[]):
        (self.people, self.selected) = (people, selected)


class ApplicationTest(unittest.TestCase):

    stub = ApplicationStub(["William", "Oliver", "Henry", "Liam"], [
        "William", "Oliver", "Henry"])

    @patch.object(Application, "__init__", return_value=None)
    def setUp(self, mock_init):
        self.application = Application()
        self.application.people = self.stub.people
        self.application.selected = self.stub.selected

    def fake_mail(self, name):
        print('Congrats, ' + name + '!')

    @patch.object(MailSystem, "send")
    @patch.object(MailSystem, "write")
    @patch.object(Application, "get_random_person")
    def test_app(self, mock_get_random_person, spy_write, spy_send):
        # mock
        mock_get_random_person.side_effect = self.application.people
        alreadySelected = self.application.selected[:]
        person = self.application.select_next_person()
        print(person + ' selected')
        self.assertNotIn(person, alreadySelected)

        # spy
        spy_write.side_effect = self.fake_mail
        self.application.notify_selected()
        self.assertEqual(spy_write.call_count, len(self.stub.selected))
        self.assertEqual(spy_send.call_count, len(self.stub.selected))

        print('\n')
        print(spy_write.call_args_list)
        print(spy_send.call_args_list)


if __name__ == "__main__":
    unittest.main()
