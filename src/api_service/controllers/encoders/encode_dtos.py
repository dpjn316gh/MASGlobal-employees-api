# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


def encode_element(element: object) -> dict:
    """
    Converts an object into a dictionary
    Args:
        element: a simple object

    Returns: a dictionary representing an object

    """
    if element is not None:
        return vars(element)
    else:
        return {}


def encode_list(elements: list) -> list:
    """
    Converts a list of simple objects into a list of dictionaries
    Args:
        elements: a list of elements

    Returns: a list of simple objects into a list of dictionaries

    """
    return [vars(e) for e in elements]
