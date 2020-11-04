def inverte_frase(frs):
    nova_frase = ""
    for inverte in frs.split(" "):
        nova_frase += inverte[::-1] + " "
    print("Frase invertida: ", format(nova_frase))

frase = str(input("Digite uma frase: "))
inverte_frase(frase)