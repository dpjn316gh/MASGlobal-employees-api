# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from unittest import TestCase, skip

from src.utils.json_rest_client import JsonRestClient


class TestJsonRestClient(TestCase):
    @skip("Integration test to test JsonRestClient")
    def test_get_request(self):
        """
        This is an integration test. It should be left on only in development mode.
        Returns:

        """
        rs = JsonRestClient("http://masglobaltestapi.azurewebsites.net/api/", "1")
        elements = rs.make_get("Employees")
        self.assertIsInstance(elements, list)

        # print(elements)

        # [{'id': 1, 'name': 'Andrea', 'contractTypeName': 'HourlySalaryEmployee', 'roleId': 1,
        #  'roleName': 'Administrator', 'roleDescription': None, 'hourlySalary': 10000.0, 'monthlySalary': 50000.0},
        # {'id': 2, 'name': 'Alex', 'contractTypeName': 'MonthlySalaryEmployee', 'roleId': 2, 'roleName': 'Contractor',
        #  'roleDescription': None, 'hourlySalary': 10000.0, 'monthlySalary': 50000.0}]
