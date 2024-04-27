from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


class TextSummary:
    """
    Class to summarize text
    """

    def __init__(
        self, text: str, above_avg_factor: float, language: str = "english"
    ) -> str:
        self.text = text
        self.stop_words = set(stopwords.words(language))
        self.above_avg_factor = above_avg_factor
        self.create_sentence_count = self._create_sentence_count()

    def _convert_to_lower_case(self, list_of_words):
        """
        returns a list where each string element in a list is converted to lowercase
        """
        return [s.lower() for s in list_of_words]

    def _remove_stopwords(self, list_of_words: list) -> list:
        """
        returns a list where each string element contained in stopwords list are removed
        """
        return [s for s in list_of_words if s not in self.stop_words]

    def _create_list_of_words(self):
        return word_tokenize(self.text)

    def _get_words(self) -> list:
        """
        Returns a list of words contained in input text string
        """
        words = self._create_list_of_words()
        words = self._convert_to_lower_case(words)
        return self._remove_stopwords(words)

    def _create_word_frequency_count(self) -> dict:
        """
        Creates frequency dictionary with count of each word
        """
        words = self._get_words()
        frequency_dict = dict()
        for word in words:
            if word in frequency_dict:
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1
        return frequency_dict

    def _get_sentences(self) -> list:
        """
        Returns list of lower case sentences
        """
        return self._convert_to_lower_case(sent_tokenize(self.text))

    def _word_in_sentence(self, sentence: str, sentences_value: dict) -> dict:
        """
        Returns a dictionary with the frequence of a word in a sentence
        """
        for word, freq in self._create_word_frequency_count().items():
            if word in sentence:
                if sentence in sentences_value:
                    sentences_value[sentence] += freq
                else:
                    sentences_value[sentence] = freq

        return sentences_value

    def _create_sentence_count(self):
        """
        Returns a dictionary with the frequence of a word in for each sentence
        """
        sentences = self._get_sentences()
        sentences_value = dict()
        for sentence in sentences:
            sentences_value = self._word_in_sentence(
                sentence=sentence, sentences_value=sentences_value
            )
        return sentences_value

    def _calculate_sum_value(self):
        """
        Returns the frequence of words in all sentences
        """
        sum_values = 0
        for sentence in self.create_sentence_count:
            sum_values += self.create_sentence_count[sentence]
        return sum_values

    def _calculate_average_values(self):
        """
        Calculate the average value per sentence
        """
        return int(self._calculate_sum_value() / len(self.create_sentence_count))

    def summarize(self):
        """
        Returns sentences with values above factor*average value
        """
        summary = ""
        for sentence in self._get_sentences():
            if (sentence in self.create_sentence_count) and (
                self.create_sentence_count[sentence]
                > (self.above_avg_factor * self._calculate_average_values())
            ):
                summary += " " + sentence
        return summary
