# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from money import Money


class Employee:
    """
    Represents a raw data from the repository
    """

    def __init__(self, employee_id: int, name: str, contract_type_name: str, role_id: int,
                 role_name: str, role_description: str, hourly_salary: Money, monthly_salary: Money):
        self.employee_id = employee_id
        self.name = name
        self.contract_type_name = contract_type_name
        self.role_id = role_id
        self.role_name = role_name
        self.role_description = role_description
        self.hourly_salary = hourly_salary
        self.monthly_salary = monthly_salary
