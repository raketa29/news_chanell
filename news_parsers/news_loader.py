import requests

from fake_useragent import UserAgent



class GalaxyParser:
    def __init__(self, url):
        self.url = url
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "user-agent": self.ua.random
        }
        self.get = self.session.get(url)

    def load_page_data(self):
        data_text = self.get.text

        return data_text


