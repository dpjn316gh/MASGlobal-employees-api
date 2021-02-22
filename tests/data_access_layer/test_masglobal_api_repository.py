# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from unittest import TestCase
from unittest.mock import MagicMock

from src.data_access_layer.repository.masglobal_api_repository import MasGlobalApiRepository, ID, NAME, \
    CONTRACT_TYPE_NAME, ROLE_ID, ROLE_NAME, ROLE_DESCRIPTION, HOURLY_SALARY, MONTHLY_SALARY


class TestMasGlobalApiRepository(TestCase):
    def test_convert_dict_to_model(self):
        raw_data = {
            'id': 1,
            'name': 'Andrea',
            'contractTypeName': 'HourlySalaryEmployee',
            'roleId': 1,
            'roleName': 'Administrator',
            'roleDescription': None,
            'hourlySalary': 10000.0,
            'monthlySalary': 50000.0}

        configuration = MagicMock()

        repository = MasGlobalApiRepository(configuration)
        employee = repository.convert_dict_to_model(raw_data)

        self.assertEqual(raw_data[ID], employee.employee_id)
        self.assertEqual(raw_data[NAME], employee.name)
        self.assertEqual(raw_data[CONTRACT_TYPE_NAME], employee.contract_type_name)
        self.assertEqual(raw_data[ROLE_ID], employee.role_id)
        self.assertEqual(raw_data[ROLE_NAME], employee.role_name)
        self.assertEqual(raw_data[ROLE_DESCRIPTION], employee.role_description)
        self.assertEqual(raw_data[HOURLY_SALARY], employee.hourly_salary)
        self.assertEqual(raw_data[MONTHLY_SALARY], employee.monthly_salary)

    def test_convert_raw_to_list_with_data(self):
        raw_data = [{'id': 1, 'name': 'Andrea', 'contractTypeName': 'HourlySalaryEmployee', 'roleId': 1,
                     'roleName': 'Administrator', 'roleDescription': None, 'hourlySalary': 10000.0,
                     'monthlySalary': 50000.0},
                    {'id': 2, 'name': 'Alex', 'contractTypeName': 'MonthlySalaryEmployee', 'roleId': 2,
                     'roleName': 'Contractor',
                     'roleDescription': None, 'hourlySalary': 10000.0, 'monthlySalary': 50000.0}]

        configuration = MagicMock()
        repository = MasGlobalApiRepository(configuration)
        employees = repository.convert_raw_to_list(raw_data)
        self.assertEqual(len(employees), 2)

    def test_convert_raw_to_list_without_data(self):
        raw_data = []
        configuration = MagicMock()
        repository = MasGlobalApiRepository(configuration)
        employees = repository.convert_raw_to_list(raw_data)
        self.assertEqual(len(employees), 0)
