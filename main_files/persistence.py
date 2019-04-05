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


def _new_shelf(filename: str):
    '''
    This method is arguably the most important function in all modules, where this function sets up the shelve for all other
    modules to use. It takes in a filename string and creates a shelve with that filename.
    '''
    local_path = os.path.join(_storage_dir, filename)
    return shelve.open(os.path.realpath(local_path), writeback=True)


class Persistence:
    '''
    This is the class that defines the persistence system as a whole, and every other module directly interacts with this
    class when grabbing or uploading objects to the quiz system.
    '''
    _shared_shelf_instance = _new_shelf("storage.dat")
    _other_shelf_instances = []

    @staticmethod
    def _cleanup():
        '''
        This method closes all of the shelves currently open. Useful for closing the quiz system in event of an error.
        '''
        Persistence._shared_shelf_instance.close()
        for shelf_instance in Persistence._other_shelf_instances:
            shelf_instance.close()

    def _wipe(self):
        '''
        This clears the shelf so it is able to be filled again with new objects. Not to be used very often as we want
        to keep the data used in the quiz system over time.
        '''
        self._shelf.clear()

    def __init__(self, filename: str = None):
        """This initializes the persistence class and creates a new persistence interface to interact with. If given a
        filename, it will create the shelf under that filename but otherwise will just add it to the currently existing shelves.

        Keyword arguments:
        filename -- optional, filename to store items to
        """
        if filename:
            self._shelf = _new_shelf(filename)
            Persistence._other_shelf_instances.append(self._shelf)
        else:
            self._shelf = Persistence._shared_shelf_instance

    def _ensure_structure_dict(self, structure_name):
        '''
        This method prevents errors from occuring when trying to grab structures from the shelf, if those structures don't
        exist. Therefore you can still run the shelf, but you would not be able to access the objects of a blank structure.

        structure_name: str
        '''
        if structure_name not in self._shelf:
            self._shelf[structure_name] = {}

    def store(self, structure: T) -> None:
        """This method stores a given structure into the shelf for the other modules to use. It takes structure as a parameter
        and makes sure it does exist in the list of structures and then adds it to the shelf.

        Keyword arguments:
        structure -- class being stored
        """
        structure_name = structure.__class__.__name__
        self._ensure_structure_dict(structure_name)
        self._shelf[structure_name][structure.id] = structure

    def retrieve(self, structure: T, structure_id: str) -> T:
        """This method is used to retrieve structures from the shelf. It takes in the structure itself, as well as the 
        name of the structure so that it can be determined from multiple structures in a module.

        Keyword arguments:
        structure -- class retrieve stored
        structure_id -- the structure unique id
        """
        structure_name = structure.__name__
        self._ensure_structure_dict(structure_name)
        if structure_id in self._shelf[structure_name]:
            return self._shelf[structure_name][structure_id]


atexit.register(Persistence._cleanup)

if __name__ == "__main__":
    p = Persistence("persist_test")
    p._wipe()

    from structures import User
    p.store(User("jackharrhy", "nice meme", "student"))

    print(p._shelf["User"].keys())
