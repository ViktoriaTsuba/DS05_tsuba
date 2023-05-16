import modules.data_downloading as ddl
import modules.data_processing as dp
import modules.data_loading as dl
import csv

url_base = 'https://quotes.toscrape.com/page/'

# --- Получение данных
data_list = ddl.get_data(5, url_base)

# --- Разбор данных
data_list = dp.scrapping_data(data_list)

# --- Запись данных в файл
dl.write_in_csv_file_from_dict(data_list, 'data\srapping_data.csv', 'w')
