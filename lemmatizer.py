from nltk import WordNetLemmatizer

l = WordNetLemmatizer()

class Lemmatizer:
    def lemmatizer(tokens):
        lemmatized_list = []
        for token in tokens:
            lemmatized_token = l.lemmatize(token)
            lemmatized_list.append(lemmatized_token)
        return lemmatized_list
