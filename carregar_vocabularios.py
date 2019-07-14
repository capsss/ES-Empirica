class Carregar_vocabularios:
    def carregar(projeto):
        tokens = []
        bigrams = []
        trigrams = []

        conteudo = open('vocabularios/' + projeto + '/tokens.txt', 'r', encoding="utf-8").read().splitlines()
        for item in conteudo:
            x = item.split('; ')
            # tokens.append([x[0], x[1]])
            tokens.append(x[0])

        conteudo = open('vocabularios/' + projeto + '/bigrams.txt', 'r', encoding="utf-8").read().splitlines()
        for item in conteudo:
            x = item.split('; ')
            b = x[0].split(', ')
            # bigrams.append([b, x[1]])
            bigrams.append(b)

        conteudo = open('vocabularios/' + projeto + '/trigrams.txt', 'r', encoding="utf-8").read().splitlines()
        for item in conteudo:
            x = item.split('; ')
            t = x[0].split(', ')
            # trigrams.append([t, x[1]])
            trigrams.append(t)

        return tokens, bigrams, trigrams