"""Persistence

Manage the storage of structures for the applications different modules.
'Structures' are classes defined within structures.py
"""
import os
from structures import *

class Persistence:
    __shelf_instance = {}


    def __init__(self):
        """Create a persistence interface."""
        self._shelf = Persistence.__shelf_instance


    def store(structure):
        """Store a given structure.

        Keyword arguments:
        structure -- class being stored
        """
        return None


    def retrive(structure, structure_id):
        """Retrive a structure.

        Keyword arguments:
        structure -- class retrivied stored
        structure_id -- the structure unique id
        """
        pass
