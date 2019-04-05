"""Persistence
Manage the storage of structures for the applications different modules.
'Structures' are classes defined within structures.py
"""
import atexit
import os
import shelve
from typing import TypeVar

T = TypeVar('T')

_storage_dir = "persistence_store"

if not os.path.exists(_storage_dir):
    os.makedirs(_storage_dir)


def _new_shelf(filename):
    local_path = os.path.join(_storage_dir, filename)
    return shelve.open(os.path.realpath(local_path), writeback=True)


class Persistence:
    _shared_shelf_instance = _new_shelf("storage.dat")
    _other_shelf_instances = []

    @staticmethod
    def _cleanup():
        Persistence._shared_shelf_instance.close()
        for shelf_instance in Persistence._other_shelf_instances:
            shelf_instance.close()

    def _wipe(self):
        self._shelf.clear()

    def __init__(self, filename: str = None):
        """Create a persistence interface.
        Keyword arguments:
        filename -- optional, filename to store items to
        """
        if filename:
            self._shelf = _new_shelf(filename)
            Persistence._other_shelf_instances.append(self._shelf)
        else:
            self._shelf = Persistence._shared_shelf_instance

    def _ensure_structure_dict(self, structure_name):
        if structure_name not in self._shelf:
            self._shelf[structure_name] = {}

    def store(self, structure: T) -> None:
        """Store a given structure.
        Keyword arguments:
        structure -- class being stored
        """
        structure_name = structure.__class__.__name__
        self._ensure_structure_dict(structure_name)
        self._shelf[structure_name][structure.id] = structure

    def retrieve(self, structure: T, structure_id: str) -> T:
        """Retrieve a structure.
        Keyword arguments:
        structure -- class retrieve stored
        structure_id -- the structure unique id
        """
        structure_name = structure.__name__
        self._ensure_structure_dict(structure_name)
        if structure_id in self._shelf[structure_name]:
            return self._shelf[structure_name][structure_id]


atexit.register(Persistence._cleanup)


