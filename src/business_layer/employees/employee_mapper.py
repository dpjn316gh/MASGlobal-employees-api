# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from src.business_layer.dtos.employee_dto import EmployeeDto
from src.data_access_layer.model.employee import Employee


def map_model_to_dto(employee: Employee) -> EmployeeDto:
    """
    Converts an employee model to an employee dto.
    Args:
        employee: employee model

    Returns: employee dto

    """
    employee_dto = EmployeeDto(employee_id=employee.employee_id,
                               name=employee.name,
                               contract_type_name=employee.contract_type_name,
                               role_id=employee.role_id,
                               role_name=employee.role_name,
                               role_description=employee.role_description,
                               hourly_salary=employee.hourly_salary,
                               monthly_salary=employee.monthly_salary)
    return employee_dto
