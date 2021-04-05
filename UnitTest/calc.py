def add(x, y):
    """Add Function"""
    return x + y 


def subtract(x, y):
    """Subtract Function"""
    return x - y 


def multiply(x, y):
    """Mulltiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not dicide by zero')
    return x / y   

