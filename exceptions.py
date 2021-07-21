
class Impossible(Exception):
    """
    Exception raised when an action is impossible to be performed.

    `Exception`: Message raised when the exception is thrown
    """


class QuitWithoutSaving(SystemExit):
    """
    An exception raised to exit the game without automatically saving.
    """
