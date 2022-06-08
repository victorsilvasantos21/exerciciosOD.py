#1 - criar a classe Personagem e usar a classe List []
#Implemente um programa em Python no qual o usuário deverá informar o nome e o poder (0 a 10) de três personagens.O programa deverá informar o nome do personagem que possuir o maior poder.

from personagem import Personagem

# programa principal
lista_personagens = []

#um método de classe sendo chamado
Personagem.popular_lista_personagens( lista_personagens, 3 )

# um método de classe sendo chamado
Personagem.exibir_lista_personagens( lista_personagens ) 
                     #um metodo de classe sendo chamado
personagem_poderoso = Personagem.mais_poderoso( lista_personagens ) 

# metodo de objeto/instancia sendo chamado
print("O personagem mais poderoso é....")
personagem_poderoso.exibir_dados()


