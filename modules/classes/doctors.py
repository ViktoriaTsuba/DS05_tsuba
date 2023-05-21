import modules.classes.animal_class as a
import csv

class Doctor():

    @staticmethod
    def get_examination(object: a.Animal):
        animal_dict = {'type' : str(object), 
                       'name' : object.get_name(),
                       'color': object.get_color(),
                       'height': object.get_height(),
                       'voice': object.voice(),
                       'speed': object.move()['result']
                       }
        return animal_dict
    
    @staticmethod
    def get_report(animal_list: list):
        file_name = 'data\doctors_examination_report.csv'
        with open(file_name, mode='w', encoding='utf-8') as f:
            columns_names = animal_list[0]().keys()
            file_writer = csv.DictWriter(f, delimiter = ",", lineterminator="\r", fieldnames=columns_names)
            file_writer.writeheader()
            for el in animal_list:
                file_writer.writerow(el())
