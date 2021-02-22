# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from src.data_access_layer.model.employee import Employee
from src.data_access_layer.repository.abstract_repository import AbstractRepository
from src.utils.json_rest_client import JsonRestClient

ID = 'id'
NAME = 'name'
CONTRACT_TYPE_NAME = 'contractTypeName'
ROLE_ID = 'roleId'
ROLE_NAME = 'roleName'
ROLE_DESCRIPTION = 'roleDescription'
HOURLY_SALARY = 'hourlySalary'
MONTHLY_SALARY = 'monthlySalary'

EMPLOYEES_RESOURCE = 'Employees'


class MasGlobalApiRepository(AbstractRepository):
    """
    Manage MASGlobal employees data
    """
    BASE_URL = 'base_url'
    TIME_OUT = 'time_out'

    def __init__(self, configuration):
        self.base_url = configuration[MasGlobalApiRepository.BASE_URL]
        self.timeout = configuration[MasGlobalApiRepository.TIME_OUT]

    def get_all(self) -> list:
        """
        Makes a call to the MASGlobal employees API
        Returns: list of employees model

        """
        jrs = JsonRestClient(self.base_url, self.timeout)
        elements = jrs.make_get(EMPLOYEES_RESOURCE)
        if elements is not None:
            return self.convert_raw_to_list(elements)
        else:
            return []

    def convert_dict_to_model(self, raw_data: dict) -> Employee:
        """
        Converts from MASGlobal employees to Employee
        Args:
            raw_data: dictionary that represents an employee

        Returns: employee model

        """
        employee = Employee(
            employee_id=raw_data[ID],
            name=raw_data[NAME],
            contract_type_name=raw_data[CONTRACT_TYPE_NAME],
            role_id=raw_data[ROLE_ID],
            role_name=raw_data[ROLE_NAME],
            role_description=raw_data[ROLE_DESCRIPTION],
            hourly_salary=raw_data[HOURLY_SALARY],
            monthly_salary=raw_data[MONTHLY_SALARY])
        return employee

    def convert_raw_to_list(self, raw_data: list) -> list:
        return [self.convert_dict_to_model(element) for element in raw_data]
