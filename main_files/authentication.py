"""authentication.py.

Contains the Authentication module
"""
import uuid
import hashlib
from persistence import Persistence
from structures import User, Class


class Authentication:
    """Manage the creation, authentication, and changing of a user."""

    def __init__(self, persist=None):
        """Create a Authentication instance."""
        if not persist:
            self._persist = Persistence()
        else:
            self._persist = persist

    def _hash_password(self, password):
        salt = uuid.uuid4().hex
        hashed = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        return hashed + ':' + salt

    def _check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        salt_and_user_password = salt.encode() + user_password.encode()
        return password == hashlib.sha256(salt_and_user_password).hexdigest()

    def add_user(self, username: str, password: str, role: str,
                 realname: str = None) -> dict:
        """Add a user to the system.

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
        """Log a user into the system.

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
        """Return User object matching username.

        Keyword arguments:
        username -- unique identifier for a user
        """
        return self._persist.retrieve(User, username)

    def change_password(self, username: str, old_password: str, new_password: str) -> dict:
        """Change a users password.

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
