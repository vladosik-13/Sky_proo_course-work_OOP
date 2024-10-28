import pytest
from src.vacancy import Vacancy
from src.list import VacancyList


class MockVacancy:
    def __init__(self, title, salary, area, description, requirement, link):
        self.title = title
        self.salary = salary
        self.area = area
        self.description = description
        self.requirement = requirement
        self.link = link

    def __str__(self):
        return f"Вакансия: {self.title}, ЗП: {self.salary}"


@pytest.fixture
def vacancy_list():
    vl = VacancyList()
    vl.add_vacancy(MockVacancy('Junior Developer', 50000, 'New York', 'Develop software', 'Python', 'link1'))
    vl.add_vacancy(MockVacancy('Senior Developer', 80000, 'San Francisco', 'Lead projects', 'Java', 'link2'))
    return vl


def test_import_vacancy_list(vacancy_list):
    new_list = [
        MockVacancy('Intern', 30000, 'Remote', 'Assist in projects', 'None', 'link3')
    ]
    vacancy_list.import_vacancy_list(new_list)
    assert len(vacancy_list.vacs_list) == 1
    assert vacancy_list.vacs_list[0].title == 'Intern'
