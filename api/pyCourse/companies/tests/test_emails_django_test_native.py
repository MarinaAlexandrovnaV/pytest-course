import json
from unittest.mock import patch
from django.core import mail
from django.test import TestCase
from django.test import Client

class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self) -> None:
        with self.settings(
            EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"
        ):
            self.assertEqual(len(mail.outbox), 0)

            mail.send_mail(
                subject="Test subject",
                message="Test message",
                from_email="nexob40917@gmail.com",
                recipient_list=["nexob40917@gmail.com"],
                fail_silently=False,
            )
            self.assertEqual(len(mail.outbox), 1)
            self.assertEqual(mail.outbox[0].subject, "Test subject")

    def test_send_email_without_arguments_should_send_empty_email(self) -> None:
        client = Client()
        with patch(
            "companies.views.send_mail"
        ) as mocked_send_mail_function:
            response = client.post(path='/send-email')
            response_content = json.loads(response.content)
            print(response_content)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['status'], 'success')
            self.assertEqual(response_content['info'], 'email sent successfully')
            mocked_send_mail_function.assert_called_with(
                subject=None,
                message=None,
                from_email="python.test123@gmail.com",
                recipient_list=["python.test123@gmail.com"],
            )
    def test_send_email_with_get_verb_should_fail(self) -> None:
        client = Client()
        response = client.get(path="/send-email")
        assert response.status_code == 405
        assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}


