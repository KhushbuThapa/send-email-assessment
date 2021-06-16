import unittest

from send_email import check_email, send_email, process_emails


class TestStringMethods(unittest.TestCase):

    def test_email_validation(self):
        self.assertTrue(check_email('khusbuthapa13@gmail.com'))

    def test_invalid_email(self):
        self.assertFalse(check_email('123@hey'), False)

    def test_send_valid_email(self):
        email_list = ['khusbuthapa13@gmail.com']
        self.assertEqual(send_email(email_list), {})

    def test_send_invalid_email(self):
        emails = []
        self.assertIsNone(send_email(emails))

    def test_success_process_email(self):
        self.assertEqual(process_emails(), "Emails sent successfully!")

    def test_process_email_failure(self):
        self.assertEqual(process_emails(emails=['12344', 'hey@,,,']), "Couldn't send even a single email.")


if __name__ == '__main__':
    unittest.main()
