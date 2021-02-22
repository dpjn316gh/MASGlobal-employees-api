# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


def read_file(file_name: str) -> list:
    """
    Read a file and return a list with its lines.
    Args:
        file_name:

    Returns:
        A list of strings with the content of a file

    """
    data = []
    with open(file_name, mode='r') as resource:
        for line in resource:
            data.append(line)
    return data
