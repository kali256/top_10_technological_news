import unittest
from news_collector import NewsCollector
from clean_keywords import CleaningFiltration
from rank_keyword import RankingKeywords


class TestCollector(unittest.TestCase):
    def setUp(self):
        self.news_collector_instance = NewsCollector()
        self.news_collector_instance.parse_url_dict()
        self.cleaning_filtration = CleaningFiltration()
        self.cleaning_filtration.clean_filtr()
        self.ranking_keyword = RankingKeywords()

    def test_head_not_empty(self):
        self.assertIsInstance(self.news_collector_instance.header_list, list)
        self.assertTrue(all(isinstance(head, str) for head in self.news_collector_instance.header_list))

    def test_filtered_dict(self):
        for key in self.cleaning_filtration.filtered_dict.keys():
            self.assertTrue(key.istitle())
            self.assertIsInstance(self.cleaning_filtration.filtered_dict[key], int)

    def test_ranking_returns_tuple(self):
        for i, name, count in self.ranking_keyword.ranking():
            with self.subTest(i=i, name=name, count=count):
                self.assertIsInstance(i, int)
                self.assertIsInstance(name, str)
                self.assertIsInstance(count, int)


if __name__ == '__main__':
    unittest.main()
