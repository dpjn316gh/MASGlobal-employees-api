# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from src.business_layer.dtos.employee_dto import EmployeeDto
from src.business_layer.employees.contracts.abstract_contract import AbstractContract
from src.business_layer.employees.contracts.hourly_contract import HourlyContract
from src.business_layer.employees.contracts.monthly_contract import MonthlyContract


class EmployeeContractFactory:
    """
    Get an specific contract by employee's contract type
    """

    def __init__(self, employee_dto: EmployeeDto):
        self.employee_dto = employee_dto

    def get_contract(self) -> AbstractContract:
        if self.employee_dto.contract_type_name == 'MonthlySalaryEmployee':
            return MonthlyContract(self.employee_dto)
        elif self.employee_dto.contract_type_name == 'HourlySalaryEmployee':
            return HourlyContract(self.employee_dto)
        else:
            raise ValueError(self.employee_dto.contract_type_name)
