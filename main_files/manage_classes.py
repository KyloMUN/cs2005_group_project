"""manage_classes.py.

Contains the ManageClasses module
"""
from persistence import Persistence
from structures import Class, User


class ManageClasses:
    """Manage the creation, and modification of a class."""

    def __init__(self, persist=None):
        """Create a Authentication instance."""
        if not persist:
            self._persist = Persistence()
        else:
            self._persist = persist

    def add_class(self, classname: str, professor: str) -> dict:
        """Add a user to the system.

        Keyword arguments:
        classname -- name of a class, example COMP 1002
        professor -- user teaching the class, must be a professor
        """
        if self._persist.retrieve(Class, classname):
            return {"success": False, "message": "Class already exists."}

        prof = self._persist.retrieve(User, professor)

        if not prof:
            return {"success": False, "message": "Professor {} doesn't exist.".format(professor)}
        elif not prof.is_role('professor'):
            return {"success": False, "message": "User {} isn't a professor.".format(professor)}

        new_class = Class(classname, professor)

        prof.classes.append(new_class.id)

        self._persist.store(prof)
        self._persist.store(new_class)
        return {"success": True, "class_id": new_class.id}

    def get_class(self, classid: str) -> Class:
        """Returns a class from the system.

        Keyword arguments:
        classid -- id of a class
        """
        _class = self._persist.retrieve(Class, classid)

        if not _class:
            return {"success": False, "message": "Class doesn't exist."}

        return _class

    def assign_class_to_user(self, username: str, class_id: str) -> dict:
        user = self._persist.retrieve(User, username)
        if not user:
            return {"success": False, "message": "User doesn't exist."}

        _class = self._persist.retrieve(Class, class_id)
        if not _class:
            return {"success": False, "message": "Class doesn't exist."}

        user.classes.append(class_id)
        _class.students.append(user.id)

        self._persist.store(user)

        return {"success": True}
