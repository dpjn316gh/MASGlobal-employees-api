# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from unittest import TestCase

from src.business_layer.employees.contracts.monthly_contract import MonthlyContract
from tests.business_layer.dtos.dummies import create_dummy_employee_dto


class TestMonthlyContract(TestCase):
    contract_type_name = 'MonthlySalaryEmployee'
    calculus = lambda x: x * 12

    def test_get_annual_salary_with_0(self):
        # Arrange
        monthly_salary = 0
        employee_dto = create_dummy_employee_dto(contract_type_name=TestMonthlyContract.contract_type_name,
                                                 monthly_salary=monthly_salary)
        contract = MonthlyContract(employee_dto)

        # Acts
        annual_salary = contract.get_annual_salary()

        # Asserts
        self.assertEqual(annual_salary, TestMonthlyContract.calculus(0))

    def test_get_annual_salary_with_10(self):
        # Arrange
        monthly_salary = 10
        employee_dto = create_dummy_employee_dto(contract_type_name=TestMonthlyContract.contract_type_name,
                                                 monthly_salary=monthly_salary)
        contract = MonthlyContract(employee_dto)

        # Acts
        annual_salary = contract.get_annual_salary()

        # Asserts
        self.assertEqual(annual_salary, TestMonthlyContract.calculus(10))

    def test_get_annual_salary_with_decimals(self):
        # Arrange
        monthly_salary = 10.1
        employee_dto = create_dummy_employee_dto(contract_type_name=TestMonthlyContract.contract_type_name,
                                                 monthly_salary=monthly_salary)
        contract = MonthlyContract(employee_dto)

        # Acts
        annual_salary = contract.get_annual_salary()

        # Asserts
        self.assertEqual(annual_salary, TestMonthlyContract.calculus(10.1))
