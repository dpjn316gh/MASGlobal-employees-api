# --------------------------------------------------------------------
# MASGlobal
# Author Jorge Porras<contacto@jorgeporras.net>
# Version: 0.0.1
# --------------------------------------------------------------------


from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """
    Represent an abstract repository
    """

    @abstractmethod
    def get_all(self):
        raise NotImplementedError("You must implement the specific repository")
