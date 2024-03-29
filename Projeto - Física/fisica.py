# Anna Carolina Ribeiro Pires Zomer Nº 24.222.012-7
# Mariah Santos Gomes Nº 24.222.027-5

#Bibliotecas utilizadas
from math import *
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calcular():
  #Inputs para a posição do robô em X e Y
  robo_x = float(entry_x.get())
  robo_y = float(entry_y.get())

  #Valores que utilizaremos para o robô
  robo_velocidade = 2.78
  robo_aceleracao = 2.78
  robo_peso = 2.78
  robo_massa = 0.278

  #Armazenar os dados da bola na Posição Y do plano cartesiano em uma lista
  lista_Y = []
  arquivo_Y = open("PosicaoBolaEmY.txt", "r")
  leitura_do_arquivo_Y = arquivo_Y.readlines()
  for linha_arquivo_Y in leitura_do_arquivo_Y:
    arquivo_Y.close()
    separacao_Y = float(linha_arquivo_Y[:-1])
    lista_Y.append(separacao_Y)

  #Armazenar os dados da bola na Posição X do plano cartesiano em uma lista
  lista_X = []
  arquivo_X = open("PosicaoBolaEmX.txt", "r")
  leitura_do_arquivo_X = arquivo_X.readlines()
  for linha_arquivo_X in leitura_do_arquivo_X:
    arquivo_X.close()
    separacao_X = float(linha_arquivo_X[:-1])
    lista_X.append(separacao_X)

  #Armazenar os dados do tempo da bola
  lista_T = []
  arquivo_T = open("TempoBola.txt", "r")
  leitura_do_arquivo_T = arquivo_T.readlines()
  for linha_arquivo_T in leitura_do_arquivo_T:
    arquivo_T.close()
    separacao_T = float(linha_arquivo_T[:-1])
    lista_T.append(separacao_T)

  #Analisando qual posição da bola estará mais perto do robô em Y
  for posicao_mais_perto_y in lista_Y:
    if posicao_mais_perto_y < robo_y:
      posicao_y = posicao_mais_perto_y
  print("Posição da bola mais perto do robô: %.3f\n" % posicao_y)

  # Descobrindo o indice da lista Y e lista X
  for indice_Y in range(len(lista_Y)):
    if lista_Y[indice_Y] == posicao_y:
      indice_Y = indice_Y + 1
      print("Indíce da lista da posição da bola em Y: %d\n" % indice_Y)
      break
  indice_X = indice_Y
  print("Indíce da lista da posição da bola em Y: %d\n" % indice_X)

  # Descobrindo o valor da lista X no indice
  for x in range(indice_X):
    posicao_x = lista_X[x]
  print("Posição da bola em X quando ela tem o valor anterior em Y: %.3f\n" %
        posicao_x)

  # Descobrindo o valor da lista T no indice
  indice_T = indice_X
  for t in range(indice_T):
    tempo_bola = lista_T[t]
  print("Tempo da bola quando está na posição determinada mais próxima do robô: %.2f\n" % tempo_bola)

  # Cálculo da distância do robô até a bola
  distancia_robo_e_bola = (((posicao_x - robo_x)**2) + ((posicao_y - robo_y)**2))
  distancia_robo_e_bola = sqrt(distancia_robo_e_bola)
  distancia_robo_e_bola = round(distancia_robo_e_bola, 3)
  print("A distância que o robô terá que percorrer sem o raio de interceptação: %.3f\n" % distancia_robo_e_bola)

  # Raio de Interceptação
  distancia_robo_e_bola = distancia_robo_e_bola - 0.11
  print("A distância que o robô terá que percorrer com o raio de interceptação: %.3f\n" % distancia_robo_e_bola)

  # Tempo em que o robô vai demorar para chegar na bola
  tempo_robo_cheguei = distancia_robo_e_bola / robo_velocidade
  tempo_robo_cheguei = round(tempo_robo_cheguei, 2)
  print("Tempo que o robô vai demorar para chegar na bola: %.2f\n" % tempo_robo_cheguei)

  # Conversão de segundo para milissegundo
  tempo_robo_cheguei = tempo_robo_cheguei * 1000

  # Descobrindo em qual quadrante o robô e a bola estão
  # Robô no primeiro quadrante
  if (robo_x >= 4.5 and robo_x <= 9.0) and (robo_y >= 3.0 and robo_y <= 6.0):
    print("O ROBÔ ESTÁ NO PRIMEIRO QUADRANTE\n")
    if (posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 3.0 and posicao_y <= 6.0):
      print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    elif (posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 3.0 and posicao_y <= 6.0):
      print("A BOLA ESTÁ NO SEGUNDO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 0 and posicao_y <= 3.0):
      print("A BOLA ESTÁ NO TERCEIRO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 0 and posicao_y <= 3.5):
      print("A BOLA ESTÁ NO QUARTO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    else:
      print("A BOLA NÃO ESTÁ NO CAMPO\n")

  # Robô no segundo quadrante
  if (robo_x >= 0 and robo_x <= 4.5) and (robo_y >= 3.0 and robo_y <= 6.0):
    print("O ROBÔ ESTÁ NO SEGUNDO QUADRANTE\n")
    if (posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 3.0 and robo_y <= 6.0):
      print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    elif (posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 3.0 and posicao_y <= 6.0):
      print("A BOLA ESTÁ NO SEGUNDO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 0 and posicao_y <= 3.0):
      print("A BOLA ESTÁ NO TERCEIRO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 0 and posicao_y <= 3.5):
      print("A BOLA ESTÁ NO QUARTO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    else:
      print("A BOLA NÃO ESTÁ NO CAMPO\n")

  # Robô no terceiro quadrante
  if (robo_x >= 0 and robo_x <= 4.5) and (robo_y >= 0 and robo_y <= 3.0):
    print("O ROBÔ ESTÁ NO TERCEIRO QUADRANTE\n")
    if (posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 3.0 and robo_y <= 6.0):
      print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    elif (posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 3.0 and posicao_y <= 6.0):
      print("A BOLA ESTÁ NO SEGUNDO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 0 and posicao_y <= 3.0):
      print("A BOLA ESTÁ NO TERCEIRO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 0 and posicao_y <= 3.5):
      print("A BOLA ESTÁ NO QUARTO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    else:
      print("A BOLA NÃO ESTÁ NO CAMPO\n")

  # Robô no quarto quadrante
  if (robo_x >= 4.5 and robo_x <= 9.0) and (robo_y >= 0 and robo_y <= 3.5):
    print("O ROBÔ ESTÁ NO QUARTO QUADRANTE\n")
    if (posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 3.0 and robo_y <= 6.0):
      print("A BOLA ESTÁ NO PRIMEIRO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    elif (posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 3.0 and posicao_y <= 6.0):
      print("A BOLA ESTÁ NO SEGUNDO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y > 0 and posicao_y <= 3.0):
      print("A BOLA ESTÁ NO TERCEIRO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA ESQUERDA\n")
    elif (posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 0 and posicao_y <= 3.5):
      print("A BOLA ESTÁ NO QUARTO QUADRANTE\n")
      print("ESTÁ MAIS PERTO DO GOL DA DIREITA\n")
    else:
      print("A BOLA NÃO ESTÁ NO CAMPO\n")

  # Cálculo para chegar no gol (GOL DA ESQUERDA)
  if ((posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 3.0 and posicao_y <= 6.0)) or ((posicao_x >= 0 and posicao_x <= 4.5) and (posicao_y >= 0 and posicao_y <= 3.0)):
    distancia_ate_o_gol = (((0.5 - posicao_x)**2) + ((3 - posicao_y)**2))
    distancia_ate_o_gol = sqrt(distancia_ate_o_gol)
    distancia_ate_o_gol = round(distancia_ate_o_gol, 3)
    print("A distância que o robô terá que percorrer para chegar até o gol da esquerda com a bola: %.3f\n" % distancia_ate_o_gol)
    # Força que ele vai ter que fazer
    forca = robo_massa * robo_aceleracao
    forca = round(forca, 3)
    print("A força que o robô vai realizar sobre a bola: %.3f\n" % forca)

    # Força de atrito cinetico
    forca_atrito_cinetico = 0.5 * robo_peso
    forca_atrito_cinetico = round(forca_atrito_cinetico, 3)
    print("A força de atrito cinético que o robô vai realizar sobre a bola: %.3f\n" % forca_atrito_cinetico)

    # Trabalho realizado
    trabalho_realizado = (forca + forca_atrito_cinetico) * distancia_ate_o_gol
    trabalho_realizado = round(trabalho_realizado, 3)
    print("O trabalho que o robô vai realizar: %.3f\n" % trabalho_realizado)

  # Cálculo para chegar no gol (GOL DA DIREITA)
  if ((posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 0 and posicao_y <= 3.0)) or ((posicao_x >= 4.5 and posicao_x <= 9.0) and (posicao_y >= 3.0 and robo_y <= 6.0)):
    distancia_ate_o_gol = (((8.5 - posicao_x)**2) + ((3 - posicao_y)**2))
    distancia_ate_o_gol = sqrt(distancia_ate_o_gol)
    distancia_ate_o_gol = round(distancia_ate_o_gol, 3)
    print("A distância que o robô terá que percorrer para chegar até o gol da direita com a bola: %.3f\n" % distancia_ate_o_gol)
    # Força que ele vai ter que fazer
    forca = robo_massa * robo_aceleracao
    forca = round(forca, 3)
    print("A força que o robô vai realizar sobre a bola: %.3f\n" % forca)

    # Força de atrito cinetico
    forca_atrito_cinetico = 0.5 * robo_peso
    forca_atrito_cinetico = round(forca_atrito_cinetico, 3)
    print("A força de atrito cinético que o robô vai realizar sobre a bola: %.3f\n" % forca_atrito_cinetico)

    # Trabalho realizado
    trabalho_realizado = (forca + forca_atrito_cinetico) * distancia_ate_o_gol
    trabalho_realizado = round(trabalho_realizado, 3)
    print("O trabalho que o robô vai realizar: %.3f\n" % trabalho_realizado)

  # Contas para os gráficos
  # Distância da origem até a bola interceptada
  distancia_bola = (((posicao_x - 1.000)**2) + ((posicao_y - 0.500)**2))
  distancia_bola = sqrt(distancia_bola)
  distancia_bola = round(distancia_bola, 3)
  print("A distância da origem da bola até a interceptação: %.3f\n" % distancia_bola)

  # Distância incial da bola
  distancia_bola_incial = (((1.010 - 1.000)**2) + ((0.508 - 0.500)**2))
  distancia_bola_incial = sqrt(distancia_bola_incial)
  distancia_bola_incial = round(distancia_bola_incial, 3)
  print("A distância da origem até o primeiro ponto da bola: %.3f\n" % distancia_bola_incial)
  
  # Distância final da bola
  distancia_bola_final = (((9.000 - 1.000)*2) + ((5.300 - 0.500)*2))
  distancia_bola_final = sqrt(distancia_bola_final)
  distancia_bola_final = round(distancia_bola_final, 3)
  print("A distância da origem até o último ponto da bola: %.3f\n" % distancia_bola_final)

  # Distância inicial robô
  distancia_inicial_robo = (((robo_x)*2) + ((robo_y)*2))
  distancia_inicial_robo = sqrt(distancia_inicial_robo)
  distancia_inicial_robo = round(distancia_inicial_robo, 3)
  print("A distância da origem até o ponto da bola: %.3f\n" % distancia_inicial_robo)

  # Velocidade média inicial da bola
  velocidade_inicial_bola = distancia_bola_incial/0.02
  velocidade_inicial_bola = round(velocidade_inicial_bola, 3)
  print("A velocidade incial da bola: %.3f\n" % velocidade_inicial_bola)

  # Velocidade média final da bola
  velocidade_final_bola = distancia_bola_final / 0.02
  velocidade_final_bola = round(velocidade_final_bola, 3)
  print("A velocidade final da bola: %.3f\n" % velocidade_final_bola)

  # Aceleração média inicial da bola
  aceleracao_inicial_bola = velocidade_inicial_bola/0.02
  aceleracao_inicial_bola = round(aceleracao_inicial_bola, 3)
  print("A aceleração incial da bola: %.3f\n" % aceleracao_inicial_bola)

  # Aceleração média final da bola
  aceleracao_final_bola = velocidade_final_bola/0.02
  aceleracao_final_bola = round(aceleracao_final_bola, 3)
  print("A aceleração final da bola: %.3f\n" % aceleracao_final_bola)

  # Gráfico 1 (Gráfico das trajetórias da bola e do robô em um plano 𝑥𝑦, até o ponto de interceptação)
  fig, ax = plt.subplots()

  # Valores pré definidos
  ball_x_inicial = 1.000
  ball_y_inicial = 0.500
  ball_x_final = 9.000
  ball_y_final = 5.300

  # Traçar os pontos e linhas no gráfico
  ax.plot([robo_x, posicao_x], [robo_y, posicao_y], color='purple',label='Trajetória do Robô')
  ax.plot([ball_x_inicial, ball_x_final], [ball_y_inicial, ball_y_final], color='black', label='Trajetória da Bola')
  ax.plot(robo_x, robo_y, color='orange', marker='o', label='Início do Robô')
  ax.plot(posicao_x, posicao_y, color='blue', marker='o', label='Fim do Robô')

  # Definir os limites do gráfico
  ax.set_xlim(
    min(robo_x, posicao_x, ball_x_inicial, ball_x_final) - 1,
    max(robo_x, posicao_x, ball_x_inicial, ball_x_final) + 1)
  ax.set_ylim(
    min(robo_y, posicao_y, ball_y_inicial, ball_y_final) - 1,
    max(robo_y, posicao_y, ball_y_inicial, ball_y_final) + 1)
  
  # Adicionar rótulos e legenda
  ax.set_xlabel('Posição X')
  ax.set_ylabel('Posição Y')
  ax.legend()
  ax.grid(True)
  plt.show()

  # Gráfico 2 (Gráfico das coordenadas 𝑥 e 𝑦 da posição da bola e do robô em função do tempo 𝑡 até o instante de interceptação;)
  fig, ax = plt.subplots()

  # Valores pré definidos
  ball_x_inicial = 1.000
  ball_y_inicial = 0.500
  ball_x_final = 9.000
  ball_y_final = 5.300

  tempo_bola_inicial = 0.00
  tempo_bola_final = 20.00

  # Traçar os pontos e linhas no gráfico
  ax.plot([0, tempo_robo_cheguei], [distancia_inicial_robo, distancia_robo_e_bola], 'r-', label='Trajetória do Robô')
  ax.plot([tempo_bola_inicial, tempo_bola_final], [distancia_bola_incial, distancia_bola_final], 'b-', label='Trajetória da Bola')

  # Definir os limites do gráfico
  ax.set_xlim(
      min(robo_x, posicao_x, ball_x_inicial, ball_x_final) - 1,
      max(robo_x, posicao_x, ball_x_inicial, ball_x_final) + 1)
  ax.set_ylim(
      min(robo_y, posicao_y, ball_y_inicial, ball_y_final) - 1,
      max(robo_y, posicao_y, ball_y_inicial, ball_y_final) + 1)

  # Adicionar rótulos e legenda
  ax.set_xlabel('Tempo')
  ax.set_ylabel('Posição')
  ax.legend()
  ax.grid(True)
  plt.show()

  # Gráfico 3 (Gráfico dos componentes 𝑣𝑥 e 𝑣𝑦 da velocidade da bola e do robô em função do tempo 𝑡 até o instante de interceptação;)
  fig, ax = plt.subplots()

  # Valores pré definidos
  ball_x_inicial = 1.000
  ball_y_inicial = 0.500
  ball_x_final = 9.000
  ball_y_final = 5.300

  tempo_bola_inicial = 0.00
  tempo_bola_final = 20.00

  # Traçar os pontos e linhas no gráfico
  ax.plot([0, tempo_robo_cheguei], [0, robo_velocidade], 'r-', label='Trajetória do Robô')
  ax.plot([tempo_bola_inicial, tempo_bola_final], [velocidade_inicial_bola, velocidade_final_bola], 'b-', label='Trajetória da Bola')

  # Definir os limites do gráfico
  ax.set_xlim(
      min(robo_x, posicao_x, ball_x_inicial, ball_x_final) - 1,
      max(robo_x, posicao_x, ball_x_inicial, ball_x_final) + 1)
  ax.set_ylim(
      min(robo_y, posicao_y, ball_y_inicial, ball_y_final) - 1,
      max(robo_y, posicao_y, ball_y_inicial, ball_y_final) + 1)

  # Adicionar rótulos e legenda
  ax.set_xlabel('Tempo')
  ax.set_ylabel('Velocidade')
  ax.legend()
  ax.grid(True)
  plt.show()
  
  # Gráfico 4 (Gráfico dos componentes 𝑎𝑥 e 𝑎𝑦 da aceleração da bola e do robô em função do tempo 𝑡 até o instante de interceptação;)
  fig, ax = plt.subplots()

  # Valores pré definidos
  ball_x_inicial = 1.000
  ball_y_inicial = 0.500
  ball_x_final = 9.000
  ball_y_final = 5.300

  tempo_bola_inicial = 0.00
  tempo_bola_final = 20.00

  # Traçar os pontos e linhas no gráfico
  ax.plot([0, tempo_robo_cheguei], [0, robo_aceleracao], 'r-', label='Trajetória do Robô')
  ax.plot([tempo_bola_inicial, tempo_bola_final], [aceleracao_inicial_bola, aceleracao_final_bola], 'b-', label='Trajetória da Bola')

  # Definir os limites do gráfico
  ax.set_xlim(
      min(robo_x, posicao_x, ball_x_inicial, ball_x_final) - 1,
      max(robo_x, posicao_x, ball_x_inicial, ball_x_final) + 1)
  ax.set_ylim(
      min(robo_y, posicao_y, ball_y_inicial, ball_y_final) - 1,
      max(robo_y, posicao_y, ball_y_inicial, ball_y_final) + 1)

  # Adicionar rótulos e legenda
  ax.set_xlabel('Tempo')
  ax.set_ylabel('Aceleração')
  ax.legend()
  ax.grid(True)
  plt.show()

  # Gráfico 5 (Gráfico da distância relativa 𝑑 entre o robô e a bola como função do tempo 𝑡 até o instante de interceptação;)
  fig, ax = plt.subplots()

  # Valores pré definidos
  ball_x_inicial = 1.000
  ball_y_inicial = 0.500
  ball_x_final = 9.000
  ball_y_final = 5.300

  # Traçar os pontos e linhas no gráfico
  ax.plot([robo_x, posicao_x], [robo_y, posicao_y], color='purple',label='Trajetória do Robô')
  ax.plot(robo_x, robo_y, color='orange', marker='o', label='Início do Robô')
  ax.plot(posicao_x, posicao_y, color='blue', marker='o', label='Fim do Robô')
  
  # Definir os limites do gráfico
  ax.set_xlim(
    min(robo_x, posicao_x, ball_x_inicial, ball_x_final) - 1,
    max(robo_x, posicao_x, ball_x_inicial, ball_x_final) + 1)
  ax.set_ylim(
    min(robo_y, posicao_y, ball_y_inicial, ball_y_final) - 1,
    max(robo_y, posicao_y, ball_y_inicial, ball_y_final) + 1)
  
  # Adicionar rótulos e legenda
  ax.set_xlabel('Posição X')
  ax.set_ylabel('Posição Y')
  ax.legend()
  ax.grid(True)
  plt.show()

root = Tk()
root.title("Cálculo de Distância do Robô")

frame = Frame(root)
frame.pack(pady=20)

label_x = Label(frame, text="Posição do robô em X:")
label_x.grid(row=0, column=0)
entry_x = Entry(frame)
entry_x.grid(row=0, column=1)

label_y = Label(frame, text="Posição do robô em Y:")
label_y.grid(row=1, column=0)
entry_y = Entry(frame)
entry_y.grid(row=1, column=1)

calculate_button = Button(root, text="Calcular", command=calcular)
calculate_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()


