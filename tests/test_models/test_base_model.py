#!/usr/bin/python3
"""Test cases for the BaseModel class."""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initializes test cases for the BaseModel class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_pycodestyle(self):
        """Test for PEP8 compliance."""
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Set up test environment."""
        pass

    def tearDown(self):
        """Tear down test environment."""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test default initialization."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test initialization with kwargs."""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test initialization with integer kwargs."""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test the save method."""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the __str__ method."""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test the to_dict method."""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test initialization with None kwargs."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """Test the 'id' attribute."""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test the 'created_at' attribute."""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test the 'updated_at' attribute."""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_uuid(self):
        """Test UUID generation."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        list_instances = [instance1, instance2, instance3]
        for instance in list_instances:
            ins_uuid = instance.id
            with self.subTest(uuid=ins_uuid):
                self.assertIs(type(ins_uuid), str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """Test the __str__ method."""
        instance6 = BaseModel()
        string_output = "[BaseModel] ({}) {}".format(instance6.id,
                                                     instance6.__dict__)
        self.assertEqual(string_output, str(instance6))


class TestCodeFormat(unittest.TestCase):
    """Test cases for code format."""
    def test_pycodestyle(self):
        """Test PEP8 compliance."""
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestDocstrings(unittest.TestCase):
    """Test cases for docstrings."""
    @classmethod
    def setup_class(self):
        """Set up class."""
        self.obj_members(BaseModel, inspect.isfunction)


if __name__ == "__main__":
    unittest.main()
