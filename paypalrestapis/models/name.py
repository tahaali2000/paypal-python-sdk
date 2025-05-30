# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper


class Name(object):

    """Implementation of the 'Name' model.

    The name of the party.

    Attributes:
        given_name (str): When the party is a person, the party's given, or
            first, name.
        surname (str): When the party is a person, the party's surname or
            family name. Also known as the last name. Required when the party
            is a person. Use also to store multiple surnames including the
            matronymic, or mother's, surname.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "given_name": 'given_name',
        "surname": 'surname'
    }

    _optionals = [
        'given_name',
        'surname',
    ]

    def __init__(self,
                 given_name=APIHelper.SKIP,
                 surname=APIHelper.SKIP):
        """Constructor for the Name class"""

        # Initialize members of the class
        if given_name is not APIHelper.SKIP:
            self.given_name = given_name 
        if surname is not APIHelper.SKIP:
            self.surname = surname 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        given_name = dictionary.get("given_name") if dictionary.get("given_name") else APIHelper.SKIP
        surname = dictionary.get("surname") if dictionary.get("surname") else APIHelper.SKIP
        # Return an object of this model
        return cls(given_name,
                   surname)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'given_name={(self.given_name if hasattr(self, "given_name") else None)!r}, '
                f'surname={(self.surname if hasattr(self, "surname") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'given_name={(self.given_name if hasattr(self, "given_name") else None)!s}, '
                f'surname={(self.surname if hasattr(self, "surname") else None)!s})')
