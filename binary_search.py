def BinarySearch(lista, search):
    Direito = len(lista)-1
    Esquerdo = 0
    while Esquerdo <= Direito:
        meio = (Direito + Esquerdo) // 2
        numero = lista[meio]
        if numero == search:
            return meio
        if search > numero:
            Esquerdo = Esquerdo + 1
        else:
            Direito = Direito-1

    return -1


lista = [1, 2, 2,2,3,4,4,4,5, 6]
index = BinarySearch(lista, 4)
print(index)
