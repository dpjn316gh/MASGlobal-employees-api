# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from unittest import TestCase

from tests.business_layer.dtos.dummies import create_dummy_employee_dto, get_dummy_employees


class TestDtosJsonEncoder(TestCase):
    def test_encoding_object_using_vars(self):
        dto = create_dummy_employee_dto("any thing", 100)
        self.assertIsInstance(vars(dto), dict)

    def test_encoding_list_using_aaa(self):
        elements = get_dummy_employees(2)
        self.assertEqual(len(elements), 2)
        # print([vars(e) for e in elements])
