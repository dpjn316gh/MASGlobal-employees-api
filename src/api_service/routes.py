# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from flask import render_template

from src.api_service.constants.controller_constants import ControllerConstants
from src.api_service.controllers.employee_controller import EmployeeController


def register_routes(webapp):
    """
        Register routes on the Flask app
    Args:
        webapp:

    """

    @webapp.route(ControllerConstants.HEALTH, methods=ControllerConstants.GET_POST)
    def health_check():
        """
        Health check route.

        Returns: Json response with 200 http code.
        """
        webapp.logger.info("Health Check")
        return {'status': 'UP'}, 200

    @webapp.route(ControllerConstants.ROOT, methods=ControllerConstants.GET_POST)
    def index():
        """
        Index show the API is running. TODO. Replace with Swagger
        Returns: a processed request

        """
        return render_template('home.html')

    @webapp.route(ControllerConstants.EMPLOYEES, methods=ControllerConstants.ONLY_GET)
    def get_all_employees():
        """
        Controls a GET of employees resource
        Returns: a processed request

        """
        employee_controller = EmployeeController()
        return employee_controller.process_all_employees()

    @webapp.route(f"{ControllerConstants.EMPLOYEES}/<int:employee_id>", methods=ControllerConstants.ONLY_GET)
    def get_employee_by_id(employee_id: int):
        """
        Controls a GET of employee/id resource
        Args:
            employee_id:

        Returns: a processed request

        """
        employee_controller = EmployeeController()
        return employee_controller.process_employee_by_id(employee_id)

    @webapp.after_request
    def add_headers(response):
        """
        It allow to process to the JQuery app
        Args:
            response:

        Returns:

        """
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        return response
