import traceback
from clean_keywords import cleaning_filtration


class RankingKeywords:
    def __init__(self):
        self.filtered_dict = cleaning_filtration.filtered_dict

    def ranking(self):
        """From the purified set of words makes up the 10 most frequently mentioned words in the IT world"""
        try:
            sorted_list = sorted(self.filtered_dict.items(), key=lambda x: x[1], reverse=True)
            for i, (name, count) in enumerate(sorted_list[:10], start=1):
                yield i, name, count
        except Exception:
            traceback.print_exc()


ranking_keyword = RankingKeywords()
ranking_keyword.ranking()