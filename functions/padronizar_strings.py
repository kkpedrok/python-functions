def padronizar_textos(objeto):
    for atributo in objeto:
        if isinstance(objeto[atributo], str):
            objeto[atributo] = objeto[atributo].lower().strip()
