# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from himl import ConfigProcessor


def load_configuration(configuration_file: str) -> dict:
    """
    Loads the configuration from a yaml file into a dictionary.
    Args:
        configuration_file:
    Returns:
        dict: All configuration loaded from a yaml file.
    """

    config_processor = ConfigProcessor()

    filters = ()  # can choose to output only specific keys
    exclude_keys = ()  # can choose to remove specific keys
    output_format = "json"  # yaml/json

    return config_processor.process(path=configuration_file,
                                    filters=filters,
                                    exclude_keys=exclude_keys,
                                    output_format=output_format,
                                    print_data=False)
