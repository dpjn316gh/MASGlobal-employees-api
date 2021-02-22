# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from src.business_layer.dtos.employee_dto import EmployeeDto
from src.business_layer.employees.employee_service import EmployeeService


class FacadeService:
    """
    Facade of services.
    It may contain several services.
    """

    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service

    def get_employee_by_id(self, employee_id: str) -> EmployeeDto:
        return self.employee_service.get_employee_by_id(employee_id)

    def get_employees_by_ids(self, employee_id: list) -> list:
        return self.employee_service.get_employees_by_ids(employee_id)

    def get_all_employees(self) -> list:
        return self.employee_service.get_all_employees()
