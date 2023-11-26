#!/usr/bin/python3
"""
Contains the TestProductDocs classes
"""

from datetime import datetime
import inspect
from models import product
from models.base_model import BaseModel
import pep8
import unittest
Product = product.Product


class TestProductDocs(unittest.TestCase):
    """Tests to check the documentation and style of Product class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.product_f = inspect.getmembers(Product, inspect.isfunction)

    def test_pep8_conformance_product(self):
        """Test that models/product.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/product.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_product(self):
        """Test that tests/test_models/test_product.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_product.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_product_module_docstring(self):
        """Test for the product.py module docstring"""
        self.assertIsNot(product.__doc__, None,
                         "product.py needs a docstring")
        self.assertTrue(len(product.__doc__) >= 1,
                        "product.py needs a docstring")

    def test_product_class_docstring(self):
        """Test for the Product class docstring"""
        self.assertIsNot(Product.__doc__, None,
                         "Product class needs a docstring")
        self.assertTrue(len(Product.__doc__) >= 1,
                        "Product class needs a docstring")

    def test_product_func_docstrings(self):
        """Test for the presence of docstrings in Product methods"""
        for func in self.product_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestProduct(unittest.TestCase):
    """Test the Product class"""
    def test_is_subclass(self):
        """Test that Product is a subclass of BaseModel"""
        product = Product()
        self.assertIsInstance(product, BaseModel)
        self.assertTrue(hasattr(product, "id"))
        self.assertTrue(hasattr(product, "created_at"))
        self.assertTrue(hasattr(product, "updated_at"))

    def test_user_id_attr(self):
        """Test that Product has attribute user_id
        and it's as an empty string"""
        product = Product()
        self.assertTrue(hasattr(product, "user_id"))
        self.assertEqual(product.user_id, "")

    def test_name_attr(self):
        """Test that Product has attribute name and it's as an empty string"""
        product = Product()
        self.assertTrue(hasattr(product, "name"))
        self.assertEqual(product.name, "")

    def test_description_attr(self):
        """Test that Product has attribute description
        and it's as an empty string"""
        product = Product()
        self.assertTrue(hasattr(product, "description"))
        self.assertEqual(product.description, "")

    def test_category_attr(self):
        """Test that Product has attribute category
        and it's as an empty string"""
        product = Product()
        self.assertTrue(hasattr(product, "category"))
        self.assertEqual(product.category, "")

    def test_sub_category_attr(self):
        """Test that Product has attribute sub_category
        and it's as an empty string"""
        product = Product()
        self.assertTrue(hasattr(product, "sub_category"))
        self.assertEqual(product.sub_category, "")

    def product_image_attr(self):
        """Test that Product has attribute product_image
        and it's as an empty string"""
        product = Product()
        self.assertTrue(hasattr(product, "product_image"))
        self.assertEqual(product.product_image, "")

    def test_price_attr(self):
        """Test that Review has attribute rating and it's 0"""
        product = Product()
        self.assertTrue(hasattr(product, "price"))
        self.assertEqual(product.price, 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Product()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in p.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Product()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Product")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        product = Product()
        string = "[Product] ({}) {}".format(product.id, product.__dict__)
        self.assertEqual(string, str(product))
