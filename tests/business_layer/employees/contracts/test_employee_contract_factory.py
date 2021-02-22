# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


import unittest

from src.business_layer.employees.contracts.employee_contract_factory import EmployeeContractFactory
from src.business_layer.employees.contracts.hourly_contract import HourlyContract
from src.business_layer.employees.contracts.monthly_contract import MonthlyContract
from tests.business_layer.dtos.dummies import create_dummy_employee_dto


class TestEmployeeContractFactory(unittest.TestCase):
    def test_return_hourly_contract_object(self):
        contract_type_name = 'HourlySalaryEmployee'

        # Arrange
        hourly_salary = 0
        employee_dto = create_dummy_employee_dto(contract_type_name=contract_type_name,
                                                 hourly_salary=hourly_salary)
        factory = EmployeeContractFactory(employee_dto)

        # Acts
        contract = factory.get_contract()

        # Asserts
        self.assertIsNotNone(contract)
        self.assertIsInstance(contract, HourlyContract)

    def test_return_hourly_contract_object(self):
        contract_type_name = 'MonthlySalaryEmployee'

        # Arrange
        hourly_salary = 0
        employee_dto = create_dummy_employee_dto(contract_type_name=contract_type_name,
                                                 hourly_salary=hourly_salary)
        factory = EmployeeContractFactory(employee_dto)

        # Acts
        contract = factory.get_contract()

        # Asserts
        self.assertIsNotNone(contract)
        self.assertIsInstance(contract, MonthlyContract)
