"""Authentication

Manage the creation, authentication, and changing of a user.
"""
from structures import User

class Authentication:
    def __init__(self, persist):
        """Create a Authentication instance.

        Keyword arguments:
        persist -- persistence instance
        """
        pass


    def add_user(self, username: str, password: str) -> dict:
        """Add a user to the system

        Keyword arguments:
        username -- unique identifier for a user
        password -- users password
        """
        return {"success": True}


    def login(self, username: str, password: str) -> dict:
        """Log a user into the system

        Keyword arguments:
        username -- unique identifier for a user
        password -- users password
        """
        return {"success": True}


    def change_password(self, username: str, new_password: str) -> dict:
        """Change a users password

        Keyword arguments:
        username -- unique identifier for a user
        password -- users password
        """
        return {"success": True}
