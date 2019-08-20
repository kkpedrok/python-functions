def remover_pontuacao(texto):
    import string
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    return(texto)

