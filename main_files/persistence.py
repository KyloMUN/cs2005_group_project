"""Persistence

Manage the storage of structures for the applications different modules.
'Structures' are classes defined within structures.py
"""
from structures import *

class Authentication:
    __shelf_instance = None

    def __init__(self):
        """Create a persistence interface."""
        self.shelf = Authentication.__shelf_instance
        return

    def store(structure, structure_instance): None
        """Store a given structure.

        Keyword arguments:
        structure -- class being stored
        structure_instance -- an instance of a said structure
        """
        return None

    def retrive(structure, structure_id):
        """Retrive a structure.

        Keyword arguments:
        structure -- class retrivied stored
        structure_id -- the structure unique id
        """
        pass
