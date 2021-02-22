# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from os.path import join


def get_configuration_file(application_path: str, config_path: str, environment: str) -> str:
    """
    Gets the file name of the configuration file.
    Args:
        application_path:
        config_path:
        environment:

    Returns:

    """
    return join(application_path, config_path, environment)
