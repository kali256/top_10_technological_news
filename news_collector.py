import concurrent.futures
import traceback
import lxml
from bs4 import BeautifulSoup
from requests import Session
from supporting_information import url_dict

print("data collection")


class NewsCollector:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) " "AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/119.0.0.0 Safari/537.36"}
        self.header_list = []
        self.cookies = Session()
        self.url_news = url_dict.items()

    def parse_url_dict(self):
        """
        Collecting data from the dictionary list with url addresses, parsing headers from websites and then adding
        the resulting headers to the "header_list" list
        """
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = []
                for key, value in self.url_news:
                    futures.append(executor.submit(self.parse_url, key, value))
                for future in concurrent.futures.as_completed(futures):
                    try:
                        news = future.result()
                        for raw_headline in news:
                            head = raw_headline.text
                            self.header_list.append(head)
                    except Exception:
                        traceback.print_exc()
                        pass
        except Exception:
            traceback.print_exc()
            pass

    def parse_url(self, key, value):
        response = self.cookies.get(key, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        news = soup.find_all(class_=value)
        return news


news_collector_instance = NewsCollector()
news_collector_instance.parse_url_dict()
