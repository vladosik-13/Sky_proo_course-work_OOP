from src.vacancy import Vacancy


def test_vacancy_initialization():
    vac = Vacancy('Junior Developer', 'http://example.com', 50000, 'New York', 'Develop software', 'Python')
    assert vac.title == 'Junior Developer'
    assert vac.link == 'http://example.com'
    assert vac.salary == 50000
    assert vac.area == 'New York'
    assert vac.description == 'Develop software'
    assert vac.requirement == 'Python'


def test_vacancy_str_method():
    vac = Vacancy('Junior Developer', 'http://example.com', 50000, 'New York', 'Develop software', 'Python')
    result = str(vac)
    assert 'Вакансия - Junior Developer' in result
    assert 'зарплата - 50000' in result
    assert 'местоположение - New York' in result
    assert 'ссылка на вакансию - http://example.com' in result


def test_vacancy_full_method():
    vac = Vacancy('Senior Developer', 'http://example.com', 80000, 'San Francisco', 'Lead projects', 'Java')
    result = vac.vac_full()
    assert 'Вакансия - Senior Developer' in result
    assert 'зарплата - 80000' in result
    assert 'местоположение - San Francisco' in result
    assert 'Lead projects' in result
    assert 'Java' in result
    assert 'ссылка - http://example.com' in result


def test_vacancy_equality():
    vac1 = Vacancy('Junior Developer', 'link1', 50000, 'Area1', 'desc1', 'req1')
    vac2 = Vacancy('Mid Developer', 'link2', 50000, 'Area2', 'desc2', 'req2')
    vac3 = Vacancy('Senior Developer', 'link3', 70000, 'Area3', 'desc3', 'req3')
    assert vac1 == vac2
    assert vac1 != vac3


def test_vacancy_comparison():
    vac1 = Vacancy('Junior Developer', 'link1', 50000, 'Area1', 'desc1', 'req1')
    vac2 = Vacancy('Mid Developer', 'link2', 60000, 'Area2', 'desc2', 'req2')
    vac3 = Vacancy('Senior Developer', 'link3', 80000, 'Area3', 'desc3', 'req3')
    assert vac1 < vac2
    assert vac2 >= vac1
    assert vac2 < vac3
    assert vac3 >= vac2
