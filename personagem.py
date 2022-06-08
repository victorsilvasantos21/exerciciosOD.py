# a classe é como um tipo, cria objetos com atributos e com serviços/metodos
class Personagem:
  nome = ""
  poder = 0

  # construtor
  def __init__(self, n, p):
    self.nome = n
    self.poder = p

  def exibir_dados(self):
   print("Personagem: ", self.nome, ". Poder: ", self.poder)
    
  # metodo de classe que exibe personagens em uma lista
  @staticmethod
  def exibir_lista_personagens(lista):
    for i in lista:
      i.exibir_dados()

  @staticmethod
  def popular_lista_personagens(lista, n):
    for i in range(0,n):
      nome_temporario = input("Digite o nome do personagem: ")
      poder_temporario = int( input("Digite o poder do personagem [0-10]: ") )
      obj_personagem = Personagem(nome_temporario, poder_temporario)
      lista.append( obj_personagem )


  @staticmethod
  def mais_poderoso(lista):
    poderoso = lista[0]
    for i in lista:
      if (i.poder > poderoso.poder):
        poderoso = i
  
    return poderoso