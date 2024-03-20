#!/usr/bin/python3
"""Test cases for the City class."""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle


class TestCity(test_basemodel):
    """Test cases for the City class."""

    def __init__(self, *args, **kwargs):
        """Initializes test cases for the City class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the 'state_id' attribute."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test the 'name' attribute."""
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestPEP8(unittest.TestCase):
    """Test cases for PEP8 compliance."""

    def test_pep8_city(self):
        """Test PEP8 style."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    @classmethod
    def setUpClass(cls):
        """Set up for test."""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """Tear down after test."""
        del cls.city

    def tearDown(self):
        """Tear down after each test."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Test PEP8 compliance."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """Check for docstrings."""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """Check City attributes."""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """Check if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """Check attribute types for City."""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """Test if the save method works."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Test if to_dict method returns a dictionary."""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
