import modules.data_processing as dp
import modules.data_loading as dl


unsorted_list = [3, 7, 1, 2, 9, 8, 4]
sorted_list = dp.get_sorted_list(unsorted_list)

file_name = 'data\lesson1105.txt'
dl.write_list_in_file(dp.get_even_val(sorted_list), file_name, 'a')
dl.write_list_in_file(dp.get_even_ind_val(sorted_list), file_name, 'a')