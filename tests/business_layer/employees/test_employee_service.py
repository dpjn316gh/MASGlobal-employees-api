# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from unittest import TestCase
from unittest.mock import MagicMock

from src.business_layer.employees.employee_service import EmployeeService
from tests.business_layer.dtos.dummies import get_dummy_employees


class TestEmployeeService(TestCase):

    def test_get_employee_by_id_with_existing_element(self):
        # Arrange
        repository = MagicMock()
        repository.get_all.return_value = get_dummy_employees(10)
        service = EmployeeService(repository)
        # Acts
        employee = service.get_employee_by_id(0)

        # Asserts
        repository.get_all.assert_called_once_with()
        self.assertIsNotNone(employee)

    def test_get_employee_by_id_without_existing_element(self):
        # Arrange
        repository = MagicMock()
        repository.get_all.return_value = get_dummy_employees(10)
        service = EmployeeService(repository)
        # Acts
        employee = service.get_employee_by_id(-1)

        # Asserts
        repository.get_all.assert_called_once_with()
        self.assertIsNone(employee)

    def test_get_employee_by_id_with_duplicate_id(self):
        # Arrange
        repository = MagicMock()

        e1 = get_dummy_employees(1)[0]
        e2 = get_dummy_employees(1)[0]

        repository.get_all.return_value = [e1, e2]
        service = EmployeeService(repository)
        # Acts
        with self.assertRaises(AssertionError):
            service.get_employee_by_id(0)

    def test_get_employees_by_ids_with_existing_element(self):
        # Arrange
        specific_ids_for_searching = [0, 2, 5, 8]
        repository = MagicMock()
        repository.get_all.return_value = get_dummy_employees(10)
        service = EmployeeService(repository)
        # Acts
        employees = service.get_employees_by_ids(specific_ids_for_searching)

        # Asserts
        repository.get_all.assert_called_once_with()
        self.assertIsNotNone(employees)
        self.assertEqual(len(employees), 4)
        employees = [e.employee_id for e in employees]
        employees.sort()
        self.assertEqual(employees, specific_ids_for_searching)

    def test_get_all_employees_with_existing_elements(self):
        # Arrange
        repository = MagicMock()
        repository.get_all.return_value = get_dummy_employees(10)
        service = EmployeeService(repository)
        # Acts
        employees = service.get_all_employees()

        # Asserts
        repository.get_all.assert_called_once_with()
        self.assertIsNotNone(employees)
        self.assertEqual(len(employees), 10)

    def test_get_all_employees_without_existing_elements(self):
        # Arrange
        repository = MagicMock()
        repository.get_all.return_value = []
        service = EmployeeService(repository)
        # Acts
        employees = service.get_all_employees()

        # Asserts
        repository.get_all.assert_called_once_with()
        self.assertIsNotNone(employees)
        self.assertEqual(len(employees), 0)
