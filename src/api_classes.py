import requests
import json
from abc import ABC, abstractmethod


class ApiGetter(ABC):
    def __init__(self, change_page, vacancy_name):
        """

        :param change_page: страница сайта, с которой получаем данные
        :param vacancy_name: ключевое слово, по которому получаем вакансии
        """
        self.change_page = change_page
        self.vacancy_name = vacancy_name

    @abstractmethod
    def get_info_from_site(self):
        """
        метод для получения данных с сайта и сохранения их в python объект
        """
        pass


class HHApi(ApiGetter):
    """
    Класс для HeadHunter
    """
    def get_info_from_site(self):
        response = requests.get("https://api.hh.ru/vacancies?page={}&per_page=100&text={}".format(self.change_page,
                                                                                                  self.vacancy_name))
        python_type = json.loads(response.text)
        vacancies_info = python_type['items']
        if len(vacancies_info) == 0:
            raise Exception('Нет информации по такой профессии')
        return vacancies_info


class SuperJobApi(ApiGetter):
    """
    Класс для SuperJob
    """
    def get_info_from_site(self):
        header = {'X-Api-App-Id':
                  'v3.r.137572422.8c53d3f4e20842cb4d9d964a79afd1b522f51060.7c2b343f0a8a63d91bd67c3d971556dafac4ed8f'}
        response = requests.get('https://api.superjob.ru/2.0/vacancies/?page={}&keyword={}&count=100'.format
                                (self.change_page, self.vacancy_name),
                                headers=header)
        python_type = json.loads(response.text)
        vacancies_info = python_type['objects']
        if len(vacancies_info) == 0:
            raise Exception('Нет информации по такой профессии')
        return vacancies_info
