def jugar(caracteres,modoJuego):
    keys = list(caracteres.keys())
    index = 0
    while index < len(keys):
        key = keys[index]
        value = caracteres[key]
        print(key, ":", value)
        index += 1