# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from src.utils.patterns.singleton import Singleton


class Configuration(metaclass=Singleton):
    """
    Contains API configuration
    """
    __instance = None

    @staticmethod
    def get_instance():
        if Configuration.__instance is not None:
            return Configuration.__instance
        raise AssertionError("This class needs to be initialized")

    def __init__(self, configuration_manager):
        self.CONFIG_DICTIONARY = configuration_manager
        self.LOGGER_FILE_CONFIGURATION = configuration_manager['log_config_file']
        self.LOGGER_FILE_NAME = configuration_manager['handlers']['file']['filename']

        self.MASGLOBAL_EMPLOYEE_API = configuration_manager['masglobal_employees_api']
        self.MASGLOBAL_EMPLOYEE_API_TIMEOUT = configuration_manager['masglobal_employees_api_timeout']

        type(self).__instance = self
