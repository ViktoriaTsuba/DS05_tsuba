from bs4 import BeautifulSoup

def get_sorted_list(unsorted_list: list) -> list:
    '''
    Функция сортировки списка по возрастанию
    
    :param unsorted_list: list - input value
    :return: list
    '''

    result_list = list()
    work_list = unsorted_list

    while len(work_list) > 0:
        n = 0
        i_for_del = 0
        for i in range(len(work_list)):
            if n < work_list[i]:
                n = work_list[i]
                i_for_del = i
        result_list.append(n)
        work_list.pop(i_for_del)
    return result_list[-1::-1]


def get_even_val(sorted_list: list) -> list:
    '''
    Функция, которая возвращает четные значения из списка
    :param sorted_list: list - input value
    :return: list
    '''

    return [el for i, el in enumerate(sorted_list) if el % 2 == 0]


def get_even_ind_val(sorted_list: list) -> list:
    '''
    Функция, которая возвращает значения из списка для четных индексов
    :param sorted_list: list - input value
    :return: list
    '''
    return [el for i, el in enumerate(sorted_list) if i % 2 == 0]


def scrapping_data (html_data: list) -> list:
    """
    Скраппинг данных
    """
    result_list = list()
    for i, el in enumerate(html_data):
        soup = BeautifulSoup(el, 'lxml')
        all_lines = soup.find_all('div', class_='quote')
        for line_i, line in enumerate(all_lines):
            line_text = line.find('span', class_='text').text
            line_author = line.find('small', class_='author').text
            line_tags = [el.text for i, el in enumerate(line.find_all('a', class_='tag'))]
            line_dict = {'page': i + 1,
                         'author': line_author,
                         'text': line_text,
                         'tags': line_tags}
            result_list.append(line_dict)
    return result_list
            