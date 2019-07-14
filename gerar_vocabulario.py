import json
from separador_texto_codigo import separar_codigo
from os import listdir
from nltk import FreqDist
from tokennizer import Tokennizer
from stop_words import Stop_words
# from stemmer import Stemmer
from lemmatizer import Lemmatizer
from n_grams import N_grams

projeto = 'jquery'
arquivos = listdir('pull requests ' + projeto)

raw = ''
for arquivo in arquivos:
    with open('pull requests ' + projeto + '/' + arquivo) as json_file:  
        data = json.load(json_file)
        raw = raw + str(data['body'])
texto, codigo = separar_codigo.separar(raw)

tokens = Tokennizer.tokenize(texto)
# stemmed_list = Stemmer.stemmer(tokens)
stop_worded_list = Stop_words.stop_words(tokens)
lemmatized_list = Lemmatizer.lemmatizer(stop_worded_list)
bigrams = N_grams.n_grams(lemmatized_list, 2)
trigrams = N_grams.n_grams(lemmatized_list, 3)

f_bi = FreqDist(bigrams)
f_tri = FreqDist(trigrams)
frequentes = FreqDist(lemmatized_list)

porcentagem = int(len(frequentes) / 10)

f = open('vocabularios/' + projeto + '/tokens.txt', 'w', encoding="utf-8")
for item in frequentes.most_common(porcentagem):
        # print(str(item[0]) + '; ' + str(item[1]))
        f.write(str(item[0]) + '; ' + str(item[1]) + '\n')
f.close()

f = open('vocabularios/' + projeto + '/bigrams.txt', 'w', encoding="utf-8")
for item in f_bi.most_common(porcentagem):
        # print(str(item[0][0]) + ', ' + str(item[0][1]) + '; ' + str(item[1]))
        f.write(str(item[0][0]) + ', ' + str(item[0][1]) + '; ' + str(item[1]) + '\n')
f.close()

f = open('vocabularios/' + projeto + '/trigrams.txt', 'w', encoding="utf-8")
for item in f_tri.most_common(porcentagem):
        # print(str(item[0][0]) + ', ' + str(item[0][1]) + ', ' + str(item[0][2]) + '; ' + str(item[1]))
        f.write(str(item[0][0]) + ', ' + str(item[0][1]) + ', ' + str(item[0][2]) + '; ' + str(item[1]) + '\n')
f.close()
