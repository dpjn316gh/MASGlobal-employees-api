# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from unittest import TestCase

from src.business_layer.employees.contracts.hourly_contract import HourlyContract
from tests.business_layer.dtos.dummies import create_dummy_employee_dto


class TestHourlyContract(TestCase):
    contract_type_name = 'HourlySalaryEmployee'
    calculus = lambda x: 120 * x * 12

    def test_get_annual_salary_with_0(self):
        # Arrange
        hourly_salary = 0
        employee_dto = create_dummy_employee_dto(contract_type_name=TestHourlyContract.contract_type_name,
                                                 hourly_salary=hourly_salary)
        contract = HourlyContract(employee_dto)

        # Acts
        annual_salary = contract.get_annual_salary()

        # Asserts
        self.assertEqual(annual_salary, TestHourlyContract.calculus(0))

    def test_get_annual_salary_with_10(self):
        # Arrange
        hourly_salary = 10
        employee_dto = create_dummy_employee_dto(contract_type_name=TestHourlyContract.contract_type_name,
                                                 hourly_salary=hourly_salary)
        contract = HourlyContract(employee_dto)

        # Acts
        annual_salary = contract.get_annual_salary()

        # Asserts
        self.assertEqual(annual_salary, TestHourlyContract.calculus(10))

    def test_get_annual_salary_with_decimals(self):
        # Arrange
        hourly_salary = 10.1
        employee_dto = create_dummy_employee_dto(contract_type_name=TestHourlyContract.contract_type_name,
                                                 hourly_salary=hourly_salary)
        contract = HourlyContract(employee_dto)

        # Acts
        annual_salary = contract.get_annual_salary()

        # Asserts
        self.assertEqual(annual_salary, TestHourlyContract.calculus(10.1))
