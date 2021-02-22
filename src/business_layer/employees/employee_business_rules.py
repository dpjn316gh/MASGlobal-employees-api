# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from src.business_layer.dtos.employee_dto import EmployeeDto
from src.business_layer.employees.contracts.employee_contract_factory import EmployeeContractFactory


def calculate_annual_salary(employee: EmployeeDto):
    """
    Business rule that calculates the annual salary for a employee.
    Args:
        employee:

    Returns: annual salary

    """
    return (EmployeeContractFactory(employee).get_contract()).get_annual_salary()
