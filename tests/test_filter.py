import pytest
from src.vacancy import Vacancy
from src.filter import VacancyFilter


class MockVacancy:
    def __init__(self, title, salary, area, description, requirement, link):
        self.title = title
        self.salary = salary
        self.area = area
        self.description = description
        self.requirement = requirement
        self.link = link


@pytest.fixture
def vacancy_filter():
    vf = VacancyFilter()
    vf.vacs = [
        MockVacancy('Junior Developer', 50000, 'New York', 'Develop software', 'Python', 'link1'),
        MockVacancy('Senior Developer', 80000, 'San Francisco', 'Lead projects', 'Java', 'link2'),
        MockVacancy('QA Engineer', 60000, 'New York', 'Test software', 'Selenium', 'link3'),
    ]
    return vf


def test_filter_salary(vacancy_filter):
    vacancy_filter.filter_salary(60000)
    assert len(vacancy_filter.vacs) == 2
    assert vacancy_filter.vacs[0].title == 'Senior Developer'
    assert vacancy_filter.vacs[1].title == 'QA Engineer'


def test_filter_title(vacancy_filter):
    vacancy_filter.filter_title('Junior')
    assert len(vacancy_filter.vacs) == 1
    assert vacancy_filter.vacs[0].title == 'Junior Developer'


def test_filter_requirement(vacancy_filter):
    vacancy_filter.filter_requirement('Python')
    assert len(vacancy_filter.vacs) == 1
    assert vacancy_filter.vacs[0].title == 'Junior Developer'


def test_filter_area(vacancy_filter):
    vacancy_filter.filter_area('New York')
    assert len(vacancy_filter.vacs) == 2
    assert all(v.area == 'New York' for v in vacancy_filter.vacs)


def test_sort_by_salary(vacancy_filter):
    vacancy_filter.sort_by_salary(direction=False)  # По возрастанию
    assert vacancy_filter.vacs[0].title == 'Junior Developer'
    assert vacancy_filter.vacs[1].title == 'QA Engineer'
    assert vacancy_filter.vacs[2].title == 'Senior Developer'

    vacancy_filter.sort_by_salary(direction=True)  # По убыванию
    assert vacancy_filter.vacs[0].title == 'Senior Developer'
    assert vacancy_filter.vacs[1].title == 'QA Engineer'
    assert vacancy_filter.vacs[2].title == 'Junior Developer'