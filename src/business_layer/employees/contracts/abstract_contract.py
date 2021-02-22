# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from abc import ABC, abstractmethod


class AbstractContract(ABC):
    """
    Represent a employee's contract
    """

    @abstractmethod
    def get_annual_salary(self):
        raise NotImplementedError("You must implement a contract")
