#!/usr/bin/python
""" holds class Product"""
from models.base_model import BaseModel


class Product(BaseModel):
    """Representation of Product """
    user_id = ""
    name = ""
    description = ""
    category = ""
    sub_category = ""
    product_image = ""
    price = 0

    def __init__(self, *args, **kwargs):
        """initializes Product"""
        super().__init__(*args, **kwargs)
