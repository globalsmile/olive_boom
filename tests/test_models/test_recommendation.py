#!/usr/bin/python3
"""
Contains the TestRecommendationDocs classes
"""

from datetime import datetime
import inspect
from models import recommendation
from models.base_model import BaseModel
import pep8
import unittest
Recommendation = recommendation.Recommendation


class TestRecommendationDocs(unittest.TestCase):
    """Tests to check the documentation and style of Recommendation class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.commend_f = inspect.getmembers(Recommendation, inspect.isfunction)

    def test_pep8_conformance_recommendation(self):
        """Test that models/recommendation.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/recommendation.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_recommendation(self):
        """Test that tests/test_models/test_recommendation.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        res = pep8s.check_files(['tests/test_models/test_recommendation.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_recommendation_module_docstring(self):
        """Test for the recommendation.py module docstring"""
        self.assertIsNot(recommendation.__doc__, None,
                         "recommendation.py needs a docstring")
        self.assertTrue(len(recommendation.__doc__) >= 1,
                        "recommendation.py needs a docstring")

    def test_recommendation_class_docstring(self):
        """Test for the Recommendation class docstring"""
        self.assertIsNot(Recommendation.__doc__, None,
                         "Recommendation class needs a docstring")
        self.assertTrue(len(Recommendation.__doc__) >= 1,
                        "Recommendation class needs a docstring")

    def test_recommendation_func_docstrings(self):
        """Test for the presence of docstrings in Recommendation methods"""
        for func in self.commend_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestRecommedation(unittest.TestCase):
    """Test the Recommendation class"""
    def test_is_subclass(self):
        """Test that Recommendation is a subclass of BaseModel"""
        recommendation = Recommendation()
        self.assertIsInstance(recommendation, BaseModel)
        self.assertTrue(hasattr(recommendation, "id"))
        self.assertTrue(hasattr(recommendation, "created_at"))
        self.assertTrue(hasattr(recommendation, "updated_at"))

    def test_user_id_attr(self):
        """Test that Recommendation has attribute user_id
        and it's as an empty string,"""
        recommendation = Recommendation()
        self.assertTrue(hasattr(recommendation, "user_id"))
        self.assertEqual(recommendation.user_id, "")

    def test_recommended_product_id_attr(self):
        """Test that Recommendation has attribute recommended_product_id
        and it's as an empty string"""
        recommendation = Recommendation()
        self.assertTrue(hasattr(recommendation, "recommended_product_id"))
        self.assertEqual(recommendation.recommended_product_id, "")

    def test_score_attr(self):
        """Test that Recommendation has attribute score and it's 0"""
        recommendation = Recommendation()
        self.assertTrue(hasattr(recommendation, "score"))
        self.assertEqual(recommendation.score, 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Recommendation()
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in am.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Recommendation()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Recommendation")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        recommendation = Recommendation()
        string = (
                "[Recommendation] ({}) {}".format(
                    recommendation.id,
                    recommendation.__dict__
                    )
                )

        self.assertEqual(string, str(recommendation))
