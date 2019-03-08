def is_authenticated(self, userid):
    """Verify user is authorized to access a method.

    userid -- person object
    """
    if userid.get_role() == "INSTRUCTOR":
        return True
    return False
