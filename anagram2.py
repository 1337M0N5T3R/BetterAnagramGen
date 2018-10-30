import random


palavra = input("Escreve uma palavra: ").lower()
palavra = [letra for letra in palavra]
anagrama = ""

for letra in range(len(palavra)):
    anagrama = anagrama + palavra.pop(random.randrange(len(palavra)))

print(anagrama)

print("\nObrigado pela visita! Espero que tenhas gostado!")

input('\nCarrega ENTER para fechar a janela.')
