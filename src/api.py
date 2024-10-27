import os
from abc import ABC, abstractmethod

import requests

from config import DATA_DIR
from src.vacansy import Vacansy


class Parser(ABC):
    """Абстрактный класс по работе с API сервисами."""

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def export_vac_list(self):
        pass

