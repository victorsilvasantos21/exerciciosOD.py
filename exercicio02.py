#2 - criar a classe Animal, usar repetição de validação
#Crie um programa em Python no qual o usuário deverá informar o nome e o tipo de cinco animais de estimação. 
#O programa deverá exibir na tela para o usuário quantos Cachorros, Gatos e Peixes foram informados.


from animal import Animal

# programa principal
lista_animais = []

#um método de classe sendo chamado
Animal.popular_lista_animais( lista_animais, 5 )

# um método de classe sendo chamado
Animal.exibir_lista_animais( lista_animais ) 

# um método de classe sendo chamado
Animal.contabilizar_tipos_animais( lista_animais )
                     