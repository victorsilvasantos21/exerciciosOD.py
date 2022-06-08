

class Animal:
  nome = "" 
  tipo = ""
  
  def __init__(self, n , t):
    self.nome = n
    self.tipo = t

  def exibir_dados(self):
   print("Animal: ", self.nome, " Tipo: ", self.tipo)


  # metodo de classe que exibe animais em uma lista
  @staticmethod
  def exibir_lista_animais(lista):
    for i in lista:
      i.exibir_dados()

  @staticmethod
  def popular_lista_animais(lista, n):
    for i in range(0,n):
      nome_temporario = input("Digite o nome do animal: ").upper() 

      while (True):
        tipo_temporario = input("Digite o tipo do animal: ").upper()
        if tipo_temporario == "CACHORRO" or tipo_temporario == "GATO" or tipo_temporario == "PEIXE":
          break
        else:
          print("Os tipos válidos para os animais são Cachorro, Gatou ou Peixe")
      
      obj_animal = Animal(nome_temporario, tipo_temporario)
      lista.append( obj_animal )

  @staticmethod
  def contabilizar_tipos_animais(lista):
    qtd_cachorro = 0
    qtd_gato = 0
    qtd_peixe = 0

    for i in lista:
      if (i.tipo == "CACHORRO"):
        qtd_cachorro = qtd_cachorro + 1
      elif (i.tipo == "GATO"):
        qtd_gato = qtd_gato + 1
      else:
        qtd_peixe = qtd_peixe + 1


    print("Total de cachorros: ", qtd_cachorro)
    print("Total de gatos: ", qtd_gato)
    print("Total de peixes: ", qtd_peixe)
    