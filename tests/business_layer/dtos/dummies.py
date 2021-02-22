# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from faker import Faker
from money import Money

from src.business_layer.dtos.employee_dto import EmployeeDto


def create_dummy_employee_dto(contract_type_name: str, hourly_salary: Money = 0,
                              monthly_salary: Money = 0) -> EmployeeDto:
    fake = Faker()
    employee_dto = EmployeeDto(employee_id=1, name=fake.name(),
                               contract_type_name=contract_type_name,
                               role_id=1,
                               role_name="Some Role",
                               role_description="Role Description",
                               hourly_salary=hourly_salary,
                               monthly_salary=monthly_salary)

    return employee_dto


def get_dummy_employees(elements: int):
    employees = list()
    for i in range(0, elements):
        employee = EmployeeDto(
            employee_id=i,
            name=f"name for {i}",
            contract_type_name="MonthlySalaryEmployee" if i % 2 == 0 else "HourlySalaryEmployee",
            role_id=f"role_id for {i}",
            role_name=f"role_name for {i}",
            role_description=f"role_description for {i}",
            hourly_salary=Money(i * 1, "COP"),
            monthly_salary=Money(i * 10, "COP"))
        employees.append(employee)

    return employees
