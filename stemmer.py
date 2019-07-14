from nltk.stem import PorterStemmer

s = PorterStemmer()

class Stemmer:
    def stemmer(tokens):
        stemmed_list = []
        for token in tokens:
            stemmeds_token = s.stem(token)
            stemmed_list.append(stemmeds_token)
        return stemmed_list
