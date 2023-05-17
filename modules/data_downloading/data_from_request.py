import requests

def get_data(page_cnt: int, url: str) -> list:
    """
    Получение данных с первых n-страниц запроса url с помощью скраппинга
    :param page_cnt: num - кол-во страниц
    :param url: str - url-адресс
    :return list
    """
    html_text = list()
    for page_number in range(1, page_cnt+1):
        url_for_req = f'{url}{str(page_number)}/'
        html_text.append(requests.get(url_for_req).text)
    return html_text