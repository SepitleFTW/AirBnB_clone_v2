#!/usr/bin/python3
"""Test cases for the State class."""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """Test cases for the State class."""

    def __init__(self, *args, **kwargs):
        """Initializes test cases for the State class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Test the 'name' attribute."""
        new = self.value()
        self.assertEqual(type(new.name), str)
