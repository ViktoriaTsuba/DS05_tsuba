import time


def func_time(func):
    def wrapper(object):
        func_name = func.__name__
        start = time.time()
        func(object)
        end = time.time()
        return {'func_name': func_name, 'result': int(end - start)}
    return wrapper

def write_in_file_dec(func):
    def wrapper(object):
        result = func(object)
        with open('data\data_function_runtime.txt', 'a') as file:
            file.write(f'{time.localtime()} <{result["func_name"]}>: {result["result"]}\n')
        return result
    return wrapper
        
    