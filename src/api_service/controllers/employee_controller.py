# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from flask import jsonify

from src.api_service.controllers.encoders.encode_dtos import encode_list, encode_element
from src.business_layer.employees.employee_service import EmployeeService
from src.business_layer.facade_service import FacadeService
from src.common.configuration import Configuration
from src.data_access_layer.repository.masglobal_api_repository import MasGlobalApiRepository


class EmployeeController:
    """
    This class controls employee's api requests
    """
    def __init__(self):
        masglobal_repository = {
            MasGlobalApiRepository.BASE_URL: Configuration.get_instance().MASGLOBAL_EMPLOYEE_API,
            MasGlobalApiRepository.TIME_OUT: Configuration.get_instance().MASGLOBAL_EMPLOYEE_API_TIMEOUT}

        repository = MasGlobalApiRepository(masglobal_repository)
        employee_service = EmployeeService(repository)
        self.facade_service = FacadeService(employee_service)

    def process_all_employees(self):
        """
        Process a get request to get all employees
        Returns: list of employees

        """
        return jsonify(encode_list(self.facade_service.get_all_employees()))

    def process_employee_by_id(self, employee_id: int):
        """
        Process a get request to get an employee by its id
        Args:
            employee_id:

        Returns: the employee's information

        """
        return jsonify(encode_element(self.facade_service.get_employee_by_id(employee_id)))
