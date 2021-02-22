# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from os import environ


def get_env_variable(variable_name: str) -> str:
    """
    Get a value from environment variables by its name.
    Args:
        variable_name:

    Returns:
        the value of a environment variable it is found by its name. Otherwise, raise a AssertionError

    """
    if variable_name not in environ:
        raise AssertionError(f"{variable_name} is not defined")
    return environ[variable_name]
