from src.api_classes import HHApi, SuperJobApi
from src.json_operations import JSon
from src.vacancy import Vacancy


def user_interaction():
    input_platform = input('Введите название сайта, с которого хотите получить информацию(HeadHunter/SuperJob): ')
    input_keyword = input('Введите ключевое слово, по которому будем получать инфу с сайта: ')
    input_page_number = int(input('С какой страницы будем получать информацию?\n'
                                  'Для получения самых свежих данных укажите пожалуйста цифру 0: '))
    input_top_number = int(input('Какое количество самых высокооплачеваемых профессий показать?'
                                 '(Только для RU-региона): '))
    input_area = input('По какому городу хотите узнать о вакансиях, отвечающих вашему запросу: ')

    if input_platform in ['hh', 'HH', 'headhunter', 'HeadHunter']:
        hh_vacancies = HHApi(input_page_number, input_keyword).get_info_from_site()
        JSon('../src/vacancies_from_hh.json', hh_vacancies).write_info()
        Vacancy.hh_create_list_of_objects('../src/vacancies_from_hh.json')
        input_region = input('Отобразить доступные вакансии из зарубежных государств '
                             'и вакансии с релокацией?(Да/Нет): ')
        if input_region == 'Да':
            hh_foreign_vacancies = [vacancy for vacancy in Vacancy.hh_list_of_objects if
                                    vacancy.salary['currency'] != 'RUR']
            print('\nДоступные вакансии зарубежом и вакансии с релокацией:')
            for job in hh_foreign_vacancies:
                print(f'{job}\n')
        hh_list = [vacancy for vacancy in Vacancy.hh_list_of_objects if vacancy.salary['to'] is not None and
                   vacancy.salary['currency'] == 'RUR']
        hh_list.sort(key=lambda x: x.salary['to'])
        hh_list.reverse()
        print('Топ вакансий:\n')
        for vacancy in hh_list[:input_top_number]:
            print(vacancy)
        hh_sorted_area = [work for work in Vacancy.hh_list_of_objects if work.area == input_area]
        if len(hh_sorted_area) == 0:
            print('В этом городе вакансий нет')
        else:
            print('В указанном городе есть следующие вакансии: ')
            for work_in_city in hh_sorted_area:
                print(work_in_city)
    elif input_platform in ['sj', 'SJ', 'Superjob', 'SuperJob']:
        sj_vacancies = SuperJobApi(input_page_number, input_keyword).get_info_from_site()
        JSon('../src/vacancies_from_sj.json', sj_vacancies).write_info()
        Vacancy.sj_create_list_of_objects('../src/vacancies_from_sj.json')
        sj_list = [vacancy for vacancy in Vacancy.sj_list_of_objects if vacancy.salary['to'] != 0
                   and vacancy.salary['currency'] == 'rub']
        sj_list.sort(key=lambda x: x.salary['to'])
        sj_list.reverse()
        print('\nТоп вакансий:')
        for vacancy_ in sj_list[:input_top_number]:
            print(vacancy_)
        sj_sorted_area = [work for work in Vacancy.sj_list_of_objects if work.area == input_area]
        if len(sj_sorted_area) == 0:
            print('В указанном городе вакансий нет')
        else:
            print('В указанном городе есть следующие вакансии: ')
            for work_in_city_ in sj_sorted_area:
                print(work_in_city_)
