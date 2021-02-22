# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from logging.config import dictConfig
from logging.handlers import TimedRotatingFileHandler
from socket import gethostname

from flask import Flask

from src.api_service.error_handlers import register_error_handlers
from src.api_service.routes import register_routes
from src.common.app_constant import AppConstant
from src.common.configuration import Configuration
from src.utils.env_var_utilities import get_env_variable
from src.utils.himl_utilites import load_configuration
from src.utils.path_utilities import get_configuration_file


def load_app_configuration(webapp):
    """
    Load setting from yaml files.
    It is mandatory that APPLICATION_PATH and ENVIRONMENT environment variables are set.
    Args:
        webapp: a new flask application

    """
    try:
        configuration_file = get_configuration_file(get_env_variable(AppConstant.APPLICATION_PATH),
                                                    AppConstant.CONFIG_PATH,
                                                    get_env_variable(AppConstant.ENVIRONMENT))
    except AssertionError as err:
        raise AssertionError(f"Before running {AppConstant.APP_NAME}, don't forget to set: {err}. See README.md")

    try:
        himl_dictionary = load_configuration(configuration_file)
    except FileNotFoundError as err:
        raise AssertionError(f"Set up a valid path for running {AppConstant.APP_NAME} don't forget to set: {err}. See "
                             f"README.md")

    configuration = Configuration(himl_dictionary)
    webapp.config.from_object(configuration)


def set_up_logger(webapp):
    """
    Set up the logger. Its configuration are in log.yaml
    """
    webapp.config[AppConstant.CONFIG_DICTIONARY][AppConstant.handlers][AppConstant.file][AppConstant.filename] = \
        webapp.config[AppConstant.LOGGER_FILE_NAME].format(gethostname())

    # This implements log rotation
    handler = TimedRotatingFileHandler(
        webapp.config[AppConstant.CONFIG_DICTIONARY][AppConstant.handlers][AppConstant.file][AppConstant.filename],
        when="h",
        interval=1,
        backupCount=5)

    dictConfig(webapp.config[AppConstant.CONFIG_DICTIONARY])


def initialize_api_app(webapp):
    """
    Start necessary components to run the web app.

    Step 1. Load api configurations
    Step 2. Set up logger
    Step 3. Register flask routes
    Step 4. Register flask error handlers
    """
    load_app_configuration(webapp)

    set_up_logger(webapp)
    webapp.logger.info(f'Starting {AppConstant.APP_NAME} with:{webapp.config}')

    register_routes(webapp)

    register_error_handlers(webapp)


#####################################################
################# API's entry point #################
#####################################################
webapp = Flask(__name__, template_folder="api_service/templates")
initialize_api_app(webapp)
