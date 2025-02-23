import json
import pytest
from unittest.mock import patch, mock_open
from src.vacancy import Vacancy
from src.file import VacancyFile


@pytest.fixture
def vacancy_file():
    # Создаем временный экземпляр VacancyFile для тестов
    return VacancyFile(filename="test_vacancies.json")


def test_read_file(vacancy_file):
    # Подготовка тестовых данных
    test_data = [
        {
            "title": "Developer",
            "salary": "1000",
            "area": "Remote",
            "description": "Develop cool stuff",
            "requirement": "Python",
            "link": "http://example.com",
        }
    ]

    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
        vacancy_file.read_file()

    assert len(vacancy_file.vacs_list) == 1
    assert isinstance(vacancy_file.vacs_list[0], Vacancy)
    assert vacancy_file.vacs_list[0].title == "Developer"


def test_import_vacancy_list(vacancy_file):
    # Подготовка нового списка вакансий
    new_vacancies = [
        Vacancy("Designer", "1200", "Office", "Design great UI", "Figma", "http://example.com/designer")
    ]

    vacancy_file.import_vacancy_list(new_vacancies)

    assert len(vacancy_file.vacs_list) == 1
    assert vacancy_file.vacs_list[0].title == "Designer"


def test_export_vacancy_list(vacancy_file):
    # Подготовка тестовых данных
    vacancy_file.vacs_list = [
        Vacancy("Tester", "800", "Remote", "Test the application", "Selenium", "http://example.com/tester")
    ]

    exported_list = vacancy_file.export_vacancy_list()

    assert len(exported_list) == 1
    assert exported_list[0].title == "Tester"
