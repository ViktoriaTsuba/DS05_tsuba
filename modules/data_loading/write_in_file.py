def write_list_in_file(work_list: list, file_name: str, write_param: str='a'):
    """
    Записть данных списка в файл
    :param work_list: list - список, который будет записан в файл
    :param file_name: str - наименование файла
    :param write_param: str - параметр для открытия файл default = 'a'
    """

    with open(file_name, write_param) as f:
        f.write(', '.join(map(str, work_list)) + '\n')