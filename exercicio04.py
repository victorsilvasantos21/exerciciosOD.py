#4
# Imagine um jogo com asteroides e uma nave de ataque, que deve destruir os asteróides que voam em todas as direções. Dessa forma, crie um programa em Python que represente
# uma lista de asteroides que deveriam ser 'inseridos' no jogo. Para isso, faça uma classe que contenha os atributos  posição x, posição y (do asteroide em
# um plano cartesiano), tamanho do asteroide (1 a 10), velocidade do asteroide (1 a 5) e energia (1 a 5). Além disso, implementar 3 construtores (sobrecarga): um vazio, 
# outro passando todos os parâmetros de um objeto tipo Asteroide, e um terceiro que constrói um asteroide com posição x e posição y. 
# O programa principal deve conter a lista de Asteroides, preenchida pelo usuário. 

from asteroide import Asteroide

# programa principal
lista_asteroides = []

#um método de classe sendo chamado
Asteroide.popular_lista_asteroides( lista_asteroides, 3 )

# um método de classe sendo chamado
Asteroide.exibir_lista_asteroides( lista_asteroides ) 

