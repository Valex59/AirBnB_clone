#!/usr/bin/python3
# This module defines the BaseModel class

class BaseModel:

    def __init__(self, *args, **kwargs):
        self.id = id

    def id(self):
        self.id = (str)uuid.uuid4()

    def created_at(self):








