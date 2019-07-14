class separar_codigo:
    def separar(raw_texto):
        lista_codigo = []
        raw_codigo = ''
        substring = ''
        ativar = False

        for i in range(len(raw_texto) -2):
            if raw_texto[i:i+3] == '```':
                if ativar:
                    ativar = False
                    substring = substring + '```'
                    lista_codigo.append(substring)
                    substring = ''
                else:
                    ativar = True
            if ativar:
                substring = substring + raw_texto[i]

        for codigo in lista_codigo:
            raw_texto = raw_texto.replace(codigo, '', 1)
            raw_codigo = raw_codigo + codigo

        return raw_texto, raw_codigo
