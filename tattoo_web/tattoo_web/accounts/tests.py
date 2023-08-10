import os

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from tattoo_web.accounts.forms import RegisterUserForm, EditUserForm
from tattoo_web.accounts.models import UserProfile
from tattoo_web.accounts.validators import validate_only_alphabetical


class UserProfileModelTestCase(TestCase):
    small_gif = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )
    uploaded = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')

    VALID_POST_DATA = {
        'username': 'TestUser',
        'email': 'email@test.com',
        'first_name': 'Test',
        'last_name': 'Test',
        'profile_picture': 'images/small.gif'
    }

    def test_create__when_valid__expect_to_be_created(self):
        test_user = UserProfile.objects.create(**self.VALID_POST_DATA)
        created_user = UserProfile.objects.get(username='TestUser')

        self.assertEqual(created_user.username, self.VALID_POST_DATA['username'])
        self.assertEqual(created_user.email, self.VALID_POST_DATA['email'])
        self.assertEqual(created_user.first_name, self.VALID_POST_DATA['first_name'])
        self.assertEqual(created_user.last_name, self.VALID_POST_DATA['last_name'])
        self.assertEqual(created_user.profile_picture, self.VALID_POST_DATA['profile_picture'])
        # self.assertIsNotNone(test_user.pk)

    def test_create__when_username_has_one_more_chr_than_max__expect_raise(self):
        invalid_data = {
            **self.VALID_POST_DATA,
            'username': 't' * UserProfile.USER_NAME_MAX_LENGTH + 't'
        }

        with self.assertRaises(ValidationError):
            test_user = UserProfile.objects.create(
                **invalid_data,
            )

            test_user.full_clean()

    def test_create__when_username_has_one_less_chr_than_min__expect_raise(self):
        invalid_data = {
            **self.VALID_POST_DATA,
            'username': 't' * (UserProfile.USER_NAME_MIN_LENGTH - 1)
        }

        with self.assertRaises(ValidationError):
            test_user = UserProfile.objects.create(
                **invalid_data,
            )

            test_user.full_clean()

    def test_create__name_does_not_contain_only_alphabetical__expect_raise(self):
        invalid_data = {
            **self.VALID_POST_DATA,
            'first_name': 'Test1'
        }

        with self.assertRaises(ValidationError):
            test_user = UserProfile.objects.create(
                **invalid_data,
            )

            test_user.full_clean()

    def test_create__when_profile_picture_more_than_size_limit__expect_raise(self):
        invalid_data = {
            **self.VALID_POST_DATA,
            'profile_picture': 'images/more_than_5mb_test.jpg'
        }

        with self.assertRaises(ValidationError):
            test_user = UserProfile.objects.create(
                **invalid_data,
            )

            test_user.full_clean()


class AccountsFormsTestCase(TestCase):
    def test_register_user__whenValid__expect_to_be_created(self):
        initial_data = {
            'username': 'TestUser1',
            'email': 'email1@test.com',
            'password1': '9XkxsTh^y5D5!2gPy&Vn',
            'password2': '9XkxsTh^y5D5!2gPy&Vn',
        }

        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'media\images',
                                  'test_img.png')

        with open(image_path, 'rb') as image_file:
            profile_picture = SimpleUploadedFile("test_img.png", image_file.read(), content_type="image/png")

        file_data = {'profile_picture': profile_picture}

        form = RegisterUserForm(data=initial_data, files=file_data)

        is_valid = form.is_valid()
        print("Form is valid:", is_valid)

        if not is_valid:
            print("Form errors:", form.errors)
            print("Non-field errors:", form.non_field_errors())

        self.assertTrue(form.is_valid())

        user = form.save()

        user = UserProfile.objects.get(pk=user.pk)

        self.assertEqual(UserProfile.objects.filter(username='TestUser1').count(), 1)

        # self.assertEqual(user.username, 'TestUser1')
        # self.assertEqual(user.email, 'email1@test.com')
        # self.assertEqual(user.profile_picture.name, 'test_img.png')   # here is changing the file name
        # self.assertEqual(user.password, '9XkxsTh^y5D5!2gPy&Vn')   # here it crypt password and I can't check it

        user.delete()

    def test_register_user__whenInvalid__expect_to_raise(self):
        initial_data = {
            'username': 'TestUser1',
            'email': 'email',
            'password1': '9XkxsTh^y5D5!2gPy&Vn',
            'password2': '9XkxsTh^y5D5!2gPy&Vn',
        }

        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'media\images',
                                  'test_img.png')

        with open(image_path, 'rb') as image_file:
            profile_picture = SimpleUploadedFile("test_img.png", image_file.read(), content_type="image/png")

        file_data = {'profile_picture': profile_picture}

        form = RegisterUserForm(data=initial_data, files=file_data)

        is_valid = form.is_valid()
        print("Form is valid:", is_valid)

        if not is_valid:
            print("Form errors:", form.errors)
            print("Non-field errors:", form.non_field_errors())

        self.assertEqual(
            form.errors['email'][0],
            "Enter a valid email address."
        )

    def test_edit_user__whenValid__expect_to_be_updated(self):
        initial_data = {
            'first_name': 'TestUser',
            'last_name': 'TestUser',
            'email': 'email@test.com',
            'profile_picture': 'images/small.gif',
        }

        user = UserProfile.objects.create(**initial_data)

        updated_data = {
            'first_name': 'UserEdit',
            'last_name': 'UserEdit',
            'email': 'user@edit.com',
            'profile_picture': 'images/small.gif',
        }

        form = EditUserForm(data=updated_data, instance=user)

        self.assertTrue(form.is_valid())

        updated_user = form.save()

        updated_user = UserProfile.objects.get(pk=user.pk)

        self.assertEqual(updated_user.first_name, 'UserEdit')
        self.assertEqual(updated_user.last_name, 'UserEdit')
        self.assertEqual(updated_user.email, 'user@edit.com')
        self.assertEqual(updated_user.profile_picture, 'images/small.gif')

        updated_user.delete()

    def test_edit_user__whenInvalid__expect_to_raise(self):
        initial_data = {
            'first_name': 'TestUser',
            'last_name': 'TestUser',
            'email': 'email@test.com',
            'profile_picture': 'images/small.gif',
        }

        user = UserProfile.objects.create(**initial_data)

        updated_data = {
            'first_name': '1UserEdit',
            'last_name': 'UserEdit',
            'email': 'user@edit.com',
            'profile_picture': 'images/small.gif',
        }

        try:
            validate_only_alphabetical(updated_data['first_name'])
        except ValidationError as e:
            self.assertEqual(str(e), "['Must contain only alphabetical letters!']")
        else:
            self.fail("ValidationError not raised")

        form = EditUserForm(data=updated_data, instance=user)

        is_valid = form.is_valid()
        print("Form is valid:", is_valid)

        if not is_valid:
            print("Form errors:", form.errors)
            print("Non-field errors:", form.non_field_errors())

        self.assertEqual(
            form.errors['first_name'][0],
            "Must contain only alphabetical letters!"
        )

        user.delete()
