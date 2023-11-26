#!/usr/bin/python
""" holds class Recommendation"""
from models.base_model import BaseModel


class Recommendation(BaseModel):
    """Representation of Recommendation """
    user_id = ""
    recommended_product_id = ""
    score = 0

    def __init__(self, *args, **kwargs):
        """initializes Recommendation"""
        super().__init__(*args, **kwargs)
