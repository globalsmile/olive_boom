#!/usr/bin/python
""" holds class comparison"""
from models.base_model import BaseModel


class Comparison(BaseModel):
    """Representation of Comparison """
    user_id = ""
    productA_id = ""
    productB_id = ""
    winner_product_id = ""

    def __init__(self, *args, **kwargs):
        """initializes  Comparison"""
        super().__init__(*args, **kwargs)
