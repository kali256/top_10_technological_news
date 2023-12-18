import traceback
from bs4 import BeautifulSoup
from requests import Session
from rank_keyword import RankingKeywords
import unittest
from tests import TestCollector


class GetGoogleNews:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                          "Safari/537.36"
        }
        self.cookies = Session()
        self.ranking_keyword = RankingKeywords()

    def get_news(self):
        """Get the 5 latest news in 'news.google.com/search' about a word from the 'rank_keywords' function and
        display the rank of the word, the frequency of mentions and the 5 latest news related to it, as well as
        saving the text to a file"""
        try:
            with open("news.txt", "w") as news_file:
                for rank, word, count in self.ranking_keyword.ranking():
                    url = f"https://news.google.com/search?q={word}&hl=en-US&gl=US&ceid=US%3Aen"
                    response = self.cookies.get(url, headers=self.headers)
                    soup = BeautifulSoup(response.text, "lxml")
                    data = soup.find_all("a", class_="JtKRv")
                    top_5 = 1
                    news_file.write(f"\n{rank} word {word} has been mentioned {count} times\n\n")
                    for head in data:
                        if top_5 == 6:
                            break
                        else:
                            news_file.write(f"{head.text}\n")
                            top_5 += 1
                    news_file.write("----------------------------------------\n")
        except Exception:
            traceback.print_exc()


get_google_news = GetGoogleNews()
get_google_news.get_news()
unittest.main()
