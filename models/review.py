#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of Review """
    user_id = ""
    product_id = ""
    rating = 0
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
