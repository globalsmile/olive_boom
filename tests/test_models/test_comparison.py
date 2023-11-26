#!/usr/bin/python3
"""
Contains the TestComparisonDocs classes
"""

from datetime import datetime
import inspect
from models import comparison
from models.base_model import BaseModel
import pep8
import unittest
Comparison = comparison.Comparison


class TestComparisonDocs(unittest.TestCase):
    """Tests to check the documentation and style of Comparison class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.comparison_f = inspect.getmembers(Comparison, inspect.isfunction)

    def test_pep8_conformance_comparison(self):
        """Test that models/comparison.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/comparison.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_comparison(self):
        """Test that tests/test_models/test_comparison.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_comparison.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_comparison_module_docstring(self):
        """Test for the comparison.py module docstring"""
        self.assertIsNot(comparison.__doc__, None,
                         "comparison.py needs a docstring")
        self.assertTrue(len(comparison.__doc__) >= 1,
                        "comparison.py needs a docstring")

    def test_comparison_class_docstring(self):
        """Test for the Comparison class docstring"""
        self.assertIsNot(Comparison.__doc__, None,
                         "Comparison class needs a docstring")
        self.assertTrue(len(Comparison.__doc__) >= 1,
                        "Comparison class needs a docstring")

    def test_comparison_func_docstrings(self):
        """Test for the presence of docstrings in Comparison methods"""
        for func in self.comparison_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestComparison(unittest.TestCase):
    """Test the Comparison class"""
    def test_is_subclass(self):
        """Test that Comparison is a subclass of BaseModel"""
        comparison = Comparison()
        self.assertIsInstance(comparison, BaseModel)
        self.assertTrue(hasattr(comparison, "id"))
        self.assertTrue(hasattr(comparison, "created_at"))
        self.assertTrue(hasattr(comparison, "updated_at"))

    def test_user_id_attr(self):
        """Test that Comparison has attribute user_id and
        it's as an empty string"""
        comparison = Comparison()
        self.assertTrue(hasattr(comparison, "user_id"))
        self.assertEqual(comparison.user_id, "")

    def test_productA_id_attr(self):
        """Test that Comparison has attribute productA_id
        and it's as an empty string"""
        comparison = Comparison()
        self.assertTrue(hasattr(comparison, "productA_id"))
        self.assertEqual(comparison.productA_id, "")

    def test_productB_id_attr(self):
        """Test that Comparison has attribute productB_id
        and it's as an empty string"""
        comparison = Comparison()
        self.assertTrue(hasattr(comparison, "productB_id"))
        self.assertEqual(comparison.productB_id, "")

    def test_winner_product_id_attr(self):
        """Test that Comparison has attribute winner_product_id
        and it's as an empty string,"""
        comparison = Comparison()
        self.assertTrue(hasattr(comparison, "winner_product_id"))
        self.assertEqual(comparison.winner_product_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = Comparison()
        new_d = s.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in s.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = Comparison()
        new_d = s.to_dict()
        self.assertEqual(new_d["__class__"], "Comparison")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        comparison = Comparison()
        re = "[Comparison] ({}) {}".format(comparison.id, comparison.__dict__)
        self.assertEqual(re, str(comparison))
