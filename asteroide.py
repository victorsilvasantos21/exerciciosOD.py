class Asteroide:
  x = 0 
  y = 0
  tamanho = 0 #1 a 10
  velocidade = 0 #1 a 5
  energia = 0 #1 a 5
  
  def __init__(self, x , y, tamanho, velocidade, energia):
    self.x = x
    self.y = y
    self.tamanho = tamanho
    self.velocidade = velocidade
    self.energia = energia

  def exibir_dados(self):
   print("x: ", self.x, " y: ", self.y, " tamanho: ", self.tamanho, " velocidade: ", self.velocidade, " energia: ", self.energia)


  # metodo de classe que exibe asteroides em uma lista
  @staticmethod
  def exibir_lista_asteroides(lista):
    for i in lista:
      i.exibir_dados()

  @staticmethod
  def popular_lista_asteroides(lista, n):
    for i in range(0,n):
      print("Dados de um asteróide")
      x = int(input("Digite o valor do eixo x: "))
      y = int(input("Digite o valor do eixo y: "))
      
      while (True):
        tamanho = int(input("Digite o tamanho do asteriode[1 a 10]: "))
        if tamanho >= 1 and tamanho <= 10:
          break
        else:
          print("O tamanho está errado, deve estar entre 1 e 10")

      while (True):
        velocidade = int(input("Digite a velocidade do asteriode[1 a 5]: "))
        if velocidade >= 1 and velocidade <= 5:
          break
        else:
          print("A velocidade está errada, deve estar entre 1 e 5")

      while (True):
        energia = int(input("Digite a energia do asteriode[1 a 5]: "))
        if energia >= 1 and energia <= 5:
          break
        else:
          print("A energia está errada, deve estar entre 1 e 5")

      print("==============================")
      
      obj_asteroide = Asteroide(x, y, tamanho, velocidade, energia)
      lista.append( obj_asteroide )