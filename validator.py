def validator(*args):
    """Checks if the values are integers and are positive"""
    for arg in args:
        if arg < 0:
            raise ValueError("Value cannot be negative")
        if not isinstance(arg, int):
            raise TypeError("Value must be aa integer")
