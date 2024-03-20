#!/usr/bin/python3
"""Test cases for the User class."""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """Test cases for the User class."""

    def __init__(self, *args, **kwargs):
        """Initializes test cases for the User class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test the 'first_name' attribute."""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test the 'last_name' attribute."""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test the 'email' attribute."""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test the 'password' attribute."""
        new = self.value()
        self.assertEqual(type(new.password), str)
