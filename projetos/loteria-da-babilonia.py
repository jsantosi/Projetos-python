try:
    numero = int(input("Entre com um número da sorte entre 1 e 15: "))

    sorte = 7

    if numero < sorte:
        print("Seu número está mais baixo que o nível de bateria do meu celular!")
        print("Tente um número maior, tipo o preço de um café gourmet!")

    elif numero > sorte:
        print("Você chutou alto, igual o preço da gasolina!")

    else:
        print("Acertô mizeravi! Você tem poderes psíquicos ou foi sorte mesmo?")

except ValueError as err:
    print("Deu ruim! Tenta um número válido, por favor!")
