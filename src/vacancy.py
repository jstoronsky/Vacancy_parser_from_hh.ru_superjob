import json


class Vacancy:
    hh_list_of_objects = []
    sj_list_of_objects = []

    def __init__(self, name, salary, reqs, responsibilities, area, employer, url):
        self.name = name
        self.salary = salary
        self.reqs = reqs
        self.responsibilities = responsibilities
        self.area = area
        self.employer = employer
        self.url = url

    @classmethod
    def hh_create_list_of_objects(cls, file):
        with open(file) as vacancies:
            python_type_vacancies = json.load(vacancies)
            for vacancy in python_type_vacancies:
                if vacancy['salary'] is not None:
                    name = vacancy['name']
                    salary = vacancy['salary']
                    reqs = vacancy['snippet']['requirement']
                    responsibilities = vacancy['snippet']['responsibility']
                    area = vacancy['area']['name']
                    employer = vacancy['employer']['name']
                    url = f'https://hh.ru/vacancy/{vacancy["id"]}'
                    cls.hh_list_of_objects.append(cls(name, salary, reqs, responsibilities, area, employer, url))

    @classmethod
    def sj_create_list_of_objects(cls, file):
        with open(file) as vacancies:
            python_type_vacancies = json.load(vacancies)
            for vacancy in python_type_vacancies:
                name = vacancy['profession']
                salary = {'from': vacancy['payment_from'], 'to': vacancy['payment_from'],
                          'currency': vacancy['currency']}
                reqs = vacancy['candidat']
                responsibilities = 'См. атрибут reqs'
                area = vacancy['town']['title']
                employer = vacancy['firm_name']
                url = vacancy['link']
                cls.sj_list_of_objects.append(cls(name, salary, reqs, responsibilities, area, employer, url))

    def __sub__(self, other):
        if self.salary is None or other.salary is None or self.salary['to'] is None or other.salary['to'] is \
                None or self.salary['to'] == 0 or other.salary['to'] == 0:
            raise Exception('Вы не можете проводить эту операцию с типом None')
        else:
            if 'ru' in self.salary['currency'].lower() and 'ru' in other.salary['currency'].lower():
                salary_1 = self.salary['to']
                salary_2 = other.salary['to']
                if salary_1 > salary_2:
                    return f'Разница в зарплате между {self.name} и {other.name} составляет {salary_1 - salary_2} ' \
                           f'{self.salary["currency"]}'
                else:
                    return f'Разница в зарплате между {self.name} и {other.name} составляет {salary_2 - salary_1} ' \
                           f'{self.salary["currency"]}'
            else:
                raise Exception('Валюты не совпадают')

    def __str__(self):
        if self.responsibilities == 'См. атрибут reqs':
            return f' |Вакансия: {self.name}\nЗарплата: {self.salary["from"]} - {self.salary["to"]} ' \
                   f'{self.salary["currency"]}\n{self.reqs}\nГород: {self.area}\n' \
                   f'Работодатель: {self.employer}\nСсылка: {self.url}\n'
        else:
            return f' |Вакансия: {self.name}\nЗарплата: {self.salary["from"]} - {self.salary["to"]} ' \
                   f'{self.salary["currency"]}\nТребования: {self.reqs}\nГород: {self.area}\n' \
                   f'Работодатель: {self.employer}\nСсылка: {self.url}\n'
