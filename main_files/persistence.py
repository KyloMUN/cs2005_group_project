"""Persistence

Manage the storage of structures for the applications different modules.
'Structures' are classes defined within structures.py
"""
import atexit
import os
import shelve
from structures import User, Quiz, Class, Question, QuestionBank

class Persistence:
    __shelf_instance = shelve.open("storage.dat")

    @staticmethod
    def cleanup():
        Persistence.__shelf_instance.close()


    def __init__(self):
        """Create a persistence interface."""
        self._shelf = Persistence.__shelf_instance


    def _ensure_structure_dict(self, structure_name):
        if not structure_name in self._shelf:
            self._shelf[structure_name] = {}


    def store(self, structure):
        """Store a given structure.

        Keyword arguments:
        structure -- class being stored
        """
        structure_name = structure.__class__.__name__
        self._ensure_structure_dict(structure_name)
        structure_store = self._shelf[structure_name]
        structure_store[structure.id] = structure


    def retrive(self, structure, structure_id):
        """Retrive a structure.

        Keyword arguments:
        structure -- class retrivied stored
        structure_id -- the structure unique id
        """
        structure_name = structure.__name__
        self._ensure_structure_dict(structure_name)
        if structure_id in self._shelf[structure_name]:
            return self._shelf[structure_name][structure_id]

atexit.register(Persistence.cleanup)

if __name__ == "__main__":
    p = Persistence()

    u = User("jackharrhy", "nice meme", "student")

    p.store(u)

    print(p._shelf.keys())

    un = p.retrive(User, u.id)
    print(un)