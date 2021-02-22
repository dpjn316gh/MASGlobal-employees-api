# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from src.business_layer.dtos.employee_dto import EmployeeDto
from src.business_layer.employees.employee_business_rules import calculate_annual_salary
from src.business_layer.employees.employee_mapper import map_model_to_dto
from src.data_access_layer.repository.abstract_repository import AbstractRepository


class EmployeeService:
    """
    Manage employees service, such a queries, etc.
    """

    def __init__(self, abstract_repository: AbstractRepository):
        self.employees = []
        self.abstract_repository = abstract_repository
        self.cache_data()

    def cache_data(self):
        """
        Retrieves data from MASGlobal api, a transform that data to dto objects and applies business rules.

        """
        # TODO Pending: Add cache, like memcached to avoid request every time to the MASGlobal api
        self.employees = list(map(map_model_to_dto, self.abstract_repository.get_all()))
        self.employees = list(map(self.apply_business_rules, self.employees))

    def apply_business_rules(self, employee_dto: EmployeeDto) -> EmployeeDto:
        """
        Apply business rules on Employee DTOs
        Args:
            employee_dto:

        Returns: an employee with settled business rules

        """
        employee_dto.annual_salary = calculate_annual_salary(employee_dto)
        # more business rules here...
        return employee_dto

    def get_employee_by_id(self, employee_id: int) -> EmployeeDto:
        """
        Get an employee by its id
        Args:
            employee_id:

        Returns: an employee by its id

        """
        result = list(filter(lambda x: x.employee_id == employee_id, self.employees))

        if len(result) == 1:
            return result[0]
        elif len(result) == 0:
            return None
        else:
            raise AssertionError(f"More than one element with id {employee_id}")

    def get_employees_by_ids(self, employee_id: list) -> list:
        """
        Gets a list employees by multiple ids.
        Args:
            employee_id:

        Returns: list of employees given multiple ids

        """
        return list(filter(lambda x: x.employee_id in employee_id, self.employees))

    def get_all_employees(self) -> list:
        """
        Gets a list employees
        Returns: list of employees

        """
        return self.employees
