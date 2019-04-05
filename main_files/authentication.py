"""authentication.py.

Contains the Authentication module
"""
import uuid
import hashlib
from persistence import Persistence
from structures import User, Class


class Authentication:
    """
    This class manages the creation, authentication, and changing of a user.
    This is vey important for out flask-based frontend, as some of the options an instructor may have include creating student users, and the
    system is responsable for seeing if this student already exists or not, as well as implementing the created student's account.
    As well, every account has the option to change their password, so this module is also responsable for the authentication of the user and their
    ability to change their password.
    """

    def __init__(self, persist=None):
        """Create a Authentication instance, and sees if you are currently in a persistence environment or not."""
        if not persist:
            self._persist = Persistence()
        else:
            self._persist = persist

    def _hash_password(self, password: str):
        '''
        This function is a safety measure, where the passwords that our system takes in will not be saved as the strings they come in as, and
        instead we run them through a hash function so that they are unseeable to anyone but the memory of the user.

        password: str
        '''
        salt = uuid.uuid4().hex
        hashed = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        return hashed + ':' + salt

    def _check_password(self, hashed_password: str, user_password: str):
        '''
        This function checks if the hashed password is the encoded version of the user's password.

        hashed_password: str
        user_password: str
        '''
        password, salt = hashed_password.split(':')
        salt_and_user_password = salt.encode() + user_password.encode()
        return password == hashlib.sha256(salt_and_user_password).hexdigest()

    def add_user(self, username: str, password: str, role: str,
                 realname: str = None) -> dict:
        """This function adds a user to the system, using their username, password, role, and real name, and throwing that all into a dictionary.

        Keyword arguments:
        username -- unique identifier for a user
        password -- users password
        role -- users initial role
        """
        if self._persist.retrieve(User, username):
            return {"success": False, "message": "User already exists."}

        hashed_password = self._hash_password(password)
        self._persist.store(User(username, hashed_password, role, realname))
        return {"success": True}

    def login(self, username: str, password: str) -> dict:
        """This function is the function used to determine if the username and password a user provides are the same as a combination of username
        and password that exists within our system, and stores that token in our system so that the user may continue to use our system correctly.

        Keyword arguments:
        username -- unique identifier for a user
        password -- users password
        """
        user = self._persist.retrieve(User, username)

        if not user:
            return {"success": False, "message": "User doesn't exist."}

        if not self._check_password(user.password, password):
            return {"success": False, "message": "Invalid password."}

        return {"success": True, "user": user}

    def return_flat_user(self, username) -> User:
        user = self._persist.retrieve(User, username)

        dereferenced_class_list = []
        for _class in user.classes:
            dereferenced_class_list.append(vars(self._persist.retrieve(Class, _class)))

        flat_user = dict(vars(user))
        flat_user["classes"] = dereferenced_class_list

        flat_user.pop("password")

        return flat_user

    def get_user(self, username: str) -> User:
        """This retrieves the User object with the same name as the username string provided from the shelve system.

        Keyword arguments:
        username -- unique identifier for a user
        """
        return self._persist.retrieve(User, username)

    def change_password(self, username: str, old_password: str, new_password: str) -> dict:
        """This function is used to authenticate the changing of a user's password. If the old password is correct, it allows the user to change
        their password to the new password provided, and stores this change in the persistence system.

        Keyword arguments:
        username -- unique identifier for a user
        old_password -- users existing password
        new_password -- users password requested password
        """
        user = self._persist.retrieve(User, username)

        if not user:
            return {"success": False, "message": "User doesn't exist."}

        if not self._check_password(user.password, old_password):
            return {"success": False, "message": "Invalid password."}

        new_hashed_password = self._hash_password(new_password)
        user.password = new_hashed_password
        self._persist.store(user)

        return {"success": True}


if __name__ == "__main__":
    a = Authentication()
    a._persist._shared_shelf_instance.clear()

    print("add user", a.add_user("jackharrhy", "foobar123", "student"))
    print("login", a.login("jackharrhy", "foobar123"))
