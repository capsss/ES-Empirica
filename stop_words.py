from nltk.corpus import stopwords

class Stop_words:
    def stop_words(tokens):
        lista_stop_words = stopwords.words('english')
        lista_final = []
        for token in tokens:
                if token not in lista_stop_words and len(token) > 2:
                        lista_final.append(token)
        return lista_final