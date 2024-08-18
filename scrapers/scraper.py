from bs4 import BeautifulSoup
import requests


class Scraper:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36",
        }


    def get_page(self, url, *args, **kwargs):
        return requests.get(url, *args, **kwargs, headers=self.headers)


    def get_soup_object(self, content):
        return BeautifulSoup(content, 'html.parser')


    def to_dict(self, headers: list, values: list):
        if len(headers) != len(values):
            raise Exception('Length of lists not equal')
        return {k:(v) for k, v in list(zip(headers, values))}


    def string_to_number(self, string: str):
        string = string.replace(',', '.').replace('R$', '').replace('%', '').replace('\n', '').strip()
        try: 
            return float(string)
        except:
            return self.clean_string(string)
        

    def clean_string(self, string: str):
        return string.replace('\n', '').lower().strip().replace(',', '.')