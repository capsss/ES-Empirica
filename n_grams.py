from nltk import ngrams

class N_grams:
    def n_grams(lista, n):
        return list(ngrams(lista, n))