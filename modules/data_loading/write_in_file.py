import csv

def write_list_in_file(work_list: list, file_name: str, file_mode: str='a'):
    """
    Записть данных списка в файл
    :param work_list: list - список, который будет записан в файл
    :param file_name: str - наименование файла
    :param file_mode: str - параметр для открытия файл default = 'a'
    """

    with open(file_name, mode) as f:
        f.write(', '.join(map(str, work_list)) + '\n')

def write_in_csv_file_from_dict(work_list: list, file_name: str, file_mode: str='w'):
    with open(file_name, mode=file_mode, encoding='utf-8') as f:
        names = work_list[0].keys()
        file_writer = csv.DictWriter(f, delimiter = ",", lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for el in work_list:
            file_writer.writerow(el)