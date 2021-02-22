# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from src.business_layer.dtos.employee_dto import EmployeeDto
from src.business_layer.employees.contracts.abstract_contract import AbstractContract


class MonthlyContract(AbstractContract):
    """
    Represents an monthly contract
    """

    def __init__(self, employee_dto: EmployeeDto):
        self.employee_dto = employee_dto

    def get_annual_salary(self):
        return self.employee_dto.monthly_salary * 12
