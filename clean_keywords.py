import traceback
from news_collector import news_collector_instance
from supporting_information import exclusion_words


class CleaningFiltration:
    def __init__(self):
        self.header_list = news_collector_instance.header_list
        self.exclusion_words = exclusion_words
        self.filtered_dict = {}

    def clean_filtr(self):
        """Splits headings into individual words and clears the list, leaving only proper names"""
        word_count = {}
        words = [words for line in self.header_list
                 for words in line.split() if line != ""]
        for word in words:
            try:
                if word not in self.exclusion_words:
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1
            except Exception:
                traceback.print_exc()
                break
        self.filtered_dict = {key: value for key, value in word_count.items() if key.istitle()}


cleaning_filtration = CleaningFiltration()
cleaning_filtration.clean_filtr()
