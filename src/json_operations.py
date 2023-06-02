from abc import ABC, abstractmethod
import json


class Json(ABC):
    def __init__(self, file, vacancies):
        """

        :param file: название файла, по которому совершаются все операции
        :param vacancies: python объект с вакансиями, который мы получили через API
        """
        self.file = file
        self.vacancies = vacancies

    @abstractmethod
    def write_info(self):
        """
        Метод для записи информации в файл
        """
        pass

    @abstractmethod
    def add_info(self):
        """
        Метод для добавления информации в файл
        """
        pass

    @abstractmethod
    def delete_info(self):
        """
        Метод для удаления всей информации из файла
        """
        pass


class JSon(Json):
    def write_info(self):
        with open(self.file, "wt") as vacancies_from_hh:
            better_format = json.dumps(self.vacancies, indent=2, ensure_ascii=False)
            vacancies_from_hh.write(better_format)

    def add_info(self):
        with open(self.file) as json_str:
            python_obj = json.load(json_str)
        for vacancy in self.vacancies:
            python_obj.append(vacancy)
        with open(self.file, 'wt') as further_json:
            empty_ll = json.dumps(python_obj, indent=2, ensure_ascii=False)
            further_json.write(empty_ll)

    def delete_info(self):
        with open(self.file, "wt") as js_file:
            js_file.truncate()
