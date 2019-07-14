from carregar_vocabularios import Carregar_vocabularios
from os import listdir
import json
from tokennizer import Tokennizer
from stop_words import Stop_words
from lemmatizer import Lemmatizer
from n_grams import N_grams

import numpy as np

projeto = 'jquery'

tokens_vocabulario, bigrams_vocabulario, trigrams_vocabulario = Carregar_vocabularios.carregar(projeto)

pull_requests = []

arquivos = listdir('pull requests ' + projeto)
ultimo = int(arquivos[0][:-5])
for n in arquivos:
        if int(n[:-5]) > ultimo:
                ultimo = int(n[:-5])

for arquivo in arquivos:
    print(arquivo[:-5])
    with open('pull requests ' + projeto + '/' + arquivo) as json_file:  
        data = json.load(json_file)
        if data['state'] == 'closed' and data['body'] != None:
                conteudo = data['body']
                tokens = Tokennizer.tokenize(conteudo)
                stop_worded_list = Stop_words.stop_words(tokens)
                lemmatized_list = stop_worded_list
                lemmatized_list = Lemmatizer.lemmatizer(stop_worded_list)
                lemmatized_list = list(set(lemmatized_list))
                aceitos = []
                for token in lemmatized_list:
                        if token in tokens_vocabulario:
                                aceitos.append(token)
                bigrams = N_grams.n_grams(lemmatized_list, 2)
                # bigrams = list(set(bigrams))
                trigrams = N_grams.n_grams(lemmatized_list, 3)
                # trigrams = list(set(trigrams))
                conjunto = {'numero' : int(arquivo[:-5]), 'tokens' : aceitos, 'bigrams' : bigrams, 'trigrams' : trigrams}
                pull_requests.append(conjunto)





tabela = np.full((ultimo + 1, ultimo + 1), -1.0)

for pr in pull_requests:
        print(pr['numero'])
        importantes = pr['tokens']
        for x in pull_requests:
                cont = 0
                for t in importantes:
                        if t in x['tokens']:
                                cont += 1
                if len(importantes) > 0:
                        tabela[pr['numero']] [x['numero']] = cont / len(importantes)


relacionados = []
quantos = 5
for i in range(len(tabela)):
        linha = tabela[i]
        maior = -2
        pos = -1
        valores = []
        posicoes = []
        for q in range(quantos):
                for j in range(len(linha)):
                        if linha[j] > maior and j != i:
                                maior = linha[j]
                                pos = j
                valores.append(maior)
                posicoes.append(pos)
                linha[pos] = 0
                maior = -2
                pos = -1
        if maior != 0.0:
                relacionados.append([i, valores, posicoes])




numeros = [771, 1320, 3113, 6, 9, 29, 53, 86, 102, 120, 138, 228, 399, 441, 502, 516, 733, 747, 810, 813, 831, 887, 902, 910, 1051, 1320, 1356,
        1450, 1505, 1523, 1571, 1579, 1618, 1644, 1837, 2180, 2454, 3069, 3078, 3081, 390, 3095, 3170, 3171, 3173, 3188, 3208, 3210, 3234, 3253, 3261, 3308, 3354,
        3412, 3428, 3435, 3462, 3464, 3486, 3494, 3557, 3601, 3617, 3619, 3661, 3669, 3671, 3673, 3702, 3707, 3757, 3821, 3840, 3844, 3885, 3895, 3916, 3919,
        3939, 3994, 4024, 4055, 4062, 4079, 4226, 4259, 4301, 4313, 4342, 4369, 4373, 4375, 4380, 4399, 4400]
for item in relacionados:
        for pr in pull_requests:
                if item[0] in numeros and item[0] == pr['numero']:
                        print('PULL REQUEST NUMERO: ' + str(pr['numero']))
                        for token in pr['tokens']:
                                print(token)
                        for i in range(len(item[1])):
                                print(str(item[2][i]) + ',', 'https://github.com/' + projeto + '/' + projeto + '/pull/' + str(item[2][i]) + ' ,', item[1][i] )
                        print()
                                    

for linha in tabela:
        for coluna in linha:
                open('vocabularios/' + projeto + '/tabela.txt', 'a').write(str(coluna) + ', ')
        open('vocabularios/' + projeto + '/tabela.txt', 'a').write(';\n')
