from abc import ABC, abstractmethod
import json


class Json(ABC):
    def __init__(self, file, vacancies):
        self.file = file
        self.vacancies = vacancies

    @abstractmethod
    def write_info(self):
        pass

    @abstractmethod
    def add_info(self):
        pass

    @abstractmethod
    def delete_info(self):
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
