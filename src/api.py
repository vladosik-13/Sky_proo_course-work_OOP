import os
from abc import ABC, abstractmethod

import requests

from config import DATA_DIR
from src.vacancy import Vacancy


class Parser(ABC):
    """Абстрактный класс по работе с API сервисами."""

    @abstractmethod
    def load_vacancies(self):
        pass

    @abstractmethod
    def export_vac_list(self):
        pass


class HH(Parser):
    """Класс для работы с API сервиса HeadHunter.
    Получает список вакансий по ключевому слову."""

    def __init__(self, filename="vacs.json"):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        self.vacancies_short = []
        self.fullname = os.path.join(DATA_DIR, filename)

    def load_vacancies(self, keyword):
        """Метод загружает вакансии с сервиса HH. Формирует из загруженных данных список объектов
        вакансий с полями: название, ссылка, зарплата, описание, требования, место."""

        self.params["text"] = keyword
        while self.params.get("page") != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        for vacancy in self.vacancies:
            if vacancy["name"]:
                title = vacancy["name"]
            else:
                title = "Не указано."

            if vacancy["alternate_url"]:
                link = vacancy["alternate_url"]
            else:
                link = "Не указано."

            if vacancy["snippet"]["responsibility"]:
                description = vacancy["snippet"]["responsibility"]
            else:
                description = "Не указано."

            if vacancy["snippet"]["requirement"]:
                requirement = vacancy["snippet"]["requirement"]
            else:
                requirement = "Не указано."

            if vacancy["salary"]:
                if vacancy["salary"]["from"]:
                    salary = vacancy["salary"]["from"]
                else:
                    salary = 0
            else:
                salary = 0

            if vacancy["area"]["name"]:
                area = vacancy["area"]["name"]
            else:
                area = "Не указано."

            self.vacancies_short.append(
                Vacancy(
                    title=title, link=link, description=description, requirement=requirement, salary=salary, area=area
                )
            )

    def export_vac_list(self):
        """Метод возвращает обработанный список вакансий."""
        return self.vacancies_short
