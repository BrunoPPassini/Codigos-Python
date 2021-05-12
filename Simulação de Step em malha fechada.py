###############################################################################################################
#
#               DIGITAL CONTROL - EE/UFSCAR
#
#   Author: André Carmona Hernandes
#   Version: 1
#   Last-Update: 31.03.2021
#
#   Info: Function to show Zero-Order Holder
#
#   These codes are used in DIGITAL CONTROL classes. You may use and study by them, however use with caution!
#
################################################################################################################
################################################################################################################
#   Forked by: Bruno Paiva Passini
#   Version: 1.1
#   Last-Update: 20.04.2021
#   Info: Modifications for personal use.
################################################################################################################

from control.matlab import *
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

Ts = 0.03 #  Definindo período
g_s = tf(2098, [1, 74, 2098, 0]) # Definindo função de transferência
g_z = c2d(g_s, Ts, method='tustin') # Fazendo função de transferência discretizada usando o método de tustin
print(f"G(z): {g_z}") # Realizando print da função de transferência

Ts = 0.03 #  Definindo período
c_s = tf([7.0482, 6.38989812], [1, 0]) # Definindo função de transferência
c_z = c2d(c_s, Ts, method='tustin') # Fazendo função de transferência discretizada usando o método de tustin
print(f"C(z): {c_z}") # Realizando print da função de transferência

########## QUESTÃO G ###########

MalhaFechadaC = ((c_s)*(g_s))/(1+(c_s)*(g_s)) # Calculando a malha fechada contínua
print(f"MalhaFechadaC(S): {MalhaFechadaC}")

print('\n\n')

MalhaFechadaD = (c_z*g_z)/(1+c_z*g_z) # Calculando a malha fechada discreta
print(f"MalhaFechadaD(z): {MalhaFechadaD}")

time_final = 3 # Estabelecendo tempo final de simulação

###### Step FT e criando vetor de tempo ####
n_cont = round(time_final / 0.03) + 1
t_cont = linspace(0, time_final, n_cont)
y_cont, t_c = step(MalhaFechadaC, t_cont)
n_points = round(time_final / Ts) + 1
time = linspace(0, time_final, n_points)
plt.plot(t_cont,y_cont, label = 'Malha Fechada', color = ('blue'), linewidth = 2) # Construção do gráfico contínuo


####### Dando step na FT discreta #############
y_dis, t_dis = step(MalhaFechadaD, time)
plt.step(time, y_dis, color = ('red'), label = 'Malha Fechada Discreta', linewidth = 1.5, where='post') # Construção do gráfico discreto


####### Moldando o gráfico ######
plt.legend(title='Sinal:')
plt.title('Amplitude x Tempo')
plt.xlabel('Tempo(s)')
plt.ylabel('Amplitude')
plt.grid(True, linestyle ='-.')
ponto1 = [0, 1.1]
ponto2 = [3, 1.1]
x_values = [ponto1[0], ponto2[0]]
y_values = [ponto1[1], ponto2[1]]
plt.plot(x_values, y_values, color = ('Green') )
#################################

plt.show()
