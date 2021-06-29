import csv
import sys
import nltk
from pathlib import Path
from optparse import OptionParser
import json

from relationaldbhandler import RelationalDbHandler


class Preprocessor:
    __PROCESSING_PATH = Path('../..') / 'data' / 'processing'
    __SLANG_WORDS_PATH = __PROCESSING_PATH / 'slang_words.json'
    __PUNCTUATION_PATH = __PROCESSING_PATH / 'punctuation.txt'

    __slang_words = {}
    __punctuation = []
    __stopwords = None

    def __init__(self):
        self.__handler = RelationalDbHandler()

        self.__slang_words = self.__read_slang_words(self.__SLANG_WORDS_PATH)
        self.__punctuation = self.__read_punctuation(self.__PUNCTUATION_PATH)
        self.__stopwords = set(nltk.corpus.stopwords.words('english'))

    @staticmethod
    def __read_slang_words(file_path: Path) -> dict:
        """
        Legge il file JSON delle slang words e lo ritorna.
        :param file_path: il path del file delle slang words.
        :return: un dizionario contenente le slang words.
        """
        with open(file_path) as json_file:
            slang_words_map = json.load(json_file)

        return slang_words_map

    @staticmethod
    def __read_punctuation(file_path: Path) -> list:
        """
        Legge il file contenente la puncuation e ritorna il suo contenuto
        incapsulato in una lista.
        :param file_path: il path del file della punctuation.
        :return: una lista contenente i segni di punteggiatura.
        """
        punctuation_list = []

        with open(file_path, 'r') as f:
            for line in f.readlines():
                punctuation_list.append(line.strip())

        return punctuation_list

    def load_data(self, raw_data) -> list:
        """
        Legge raw_data una linea per volta e la carica in una lista.
        :return: una lista contenente i dati in raw_data
        """
        emoSN = []

        with open(options.input, "r", encoding="utf-8") as dataset:
            for line in dataset:
                emoSN.append(line)

            print("finished!")
            return emoSN

    def preprocess(self, raw_data):
        """
        It preprocess the raw_data removing all the '-' in the composite words.
        :param raw_data:
        :return:
        """
        preprocessed_data = []

        for line in raw_data:
            if "_" not in line:
                preprocessed_data.append(line)

        print("{0} ok!".format(len(preprocessed_data)))

    def get(self):
        # Semplici print di controllo. TODO: rimuoverlo.
        print("SLANG: {0}".format(self.__slang_words))
        print("PUNCTUATION: {0}".format(self.__punctuation))
        print("STOPWORDS: {0}".format(self.__stopwords))


if __name__ == "__main__":
    sentiment_path = Path('../..') / 'data' / 'lexical-resources' / 'Sentiments'
    anger_p = sentiment_path / "Anger" / "EmoSN_anger.txt"
    output_p = Path('../..') / 'output'

    argv = sys.argv[1:]
    parser = OptionParser()

    parser.add_option("-i", "--input", help='input file', action="store", type="string", dest="input",
                      default=anger_p)

    parser.add_option("-o", "--output", help='output directory', action="store", type="string", dest="output",
                      default=output_p / "Es1/")

    (options, args) = parser.parse_args()

    # Parte nuova
    prep = Preprocessor()
    prep.get()  # TODO: debug toglierlo

    data = prep.load_data(options.input)
    prep.preprocess(data)

    if options.input is None:
        print("Missing mandatory parameters")
        sys.exit(2)