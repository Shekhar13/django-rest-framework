from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_succesful(self):
        #testing create new user with email is successful
        email = "shekhar@gmail.com"
        password = "Testpassword123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_create_user_email_normalise(self):
        # Normalise the user email
        email = 'shekhar@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email,
            "test123"
        )
        self.assertEqual(user.email, email.lower())
    # def test_create_new_superuser(self):
    #     "Test creating a new super user"
    #     user = get_user_model().objects.create_user(
    #         'test@gmail.com',
    #         "test123"
    #     )
    #     self.assertTrue(user.is_superuser)
    #     self.assertTrue(user.is_staff)
    def test_new_user_invalid_email(self):
        "Test creating user with no email raises error"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")