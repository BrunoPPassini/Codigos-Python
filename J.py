###############################################################################################################
#
#               DIGITAL CONTROL - EE/UFSCAR
#
#   Author: Bruno Paiva Passini
#   Version: 1
#   Last-Update: 23.04.2021
#
#   Info: Questão J
#
#   These codes are used in DIGITAL CONTROL classes. You may use and study by them, however use with caution!
#
################################################################################################################

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np
import control
from scipy import integrate

s=control.tf('s')
Ts = 0.03 #  Definindo período
g_s = ((2098)/(s**3+74*s**2+2098*s)) # Definindo função de transferência

z=control.tf('z')
ds = (2/0.03)*((1-z**(-1))/(1+z**(-1)))  # Discretizando usando método de tustin
g_z_v = control.minreal(2098/(ds**2+74*ds+2098))  #Função de transferência da velocidade
g_z = control.minreal((g_z_v/ds)) # Função discreta da posição

#g_z = c2d(g_s, Ts, method='tustin') # Fazendo função de transferência discretizada usando o método de tustin
#print(f"G(z): {g_z}") # Realizando print da função de transferência

Ts = 0.03 #  Definindo período
#c_s = tf([1.782, 29.9109, 37.5081], [1, 0]) # Definindo função de transferência

c_s=(((s+15.42)*(s+1.365)/(s)*1.782))
c_z =control.minreal((((ds+15.42)*(ds+1.365)/(ds)*1.782)))
#c_z = c2d(c_s, Ts, method='tustin') # Fazendo função de transferência discretizada usando o método de tustin
#print(f"C(z): {c_z}") # Realizando print da função de transferência

MalhaFechadaC = ((c_s)*(g_s))/(1+(c_s)*(g_s)) # Calculando a malha fechada contínua
print(f"MalhaFechadaC(S): {MalhaFechadaC}")

print('\n\n')

MalhaFechadaD = (c_z*g_z)/(1+c_z*g_z) # Calculando a malha fechada discreta
#print(f"MalhaFechadaD(z): {MalhaFechadaD}")

########## QUESTÃO J ###########

##########################################################################
####### Gráfico da aceleração ##################

plt.figure()
n_cont = round(2.4/0.03)+1
t_cont = linspace(0, 2.4, n_cont)
a = np.zeros(n_cont)
a[t_cont < 0.3] = 1
a[t_cont > 2.1] = -1
plt.plot(t_cont, a, label = 'a', color = ('blue'), linewidth = 2)

####### Moldando o gráfico da aceleração ######
plt.legend(title='Sinal:')
plt.title('Amplitude x Tempo')
plt.xlabel('Tempo(s)')
plt.ylabel('Aceleração')
plt.grid(True, linestyle ='-.')

###########################################################################
####### Gráfico da velocidade ##################
v = integrate.cumtrapz(a, t_cont, initial=0)  # Integrando usando a função cumptrapz

plt.figure()
plt.plot(t_cont, v, label = 'v', color = ('blue'), linewidth = 2)

####### Moldando o gráfico da velocidade ######
plt.legend(title='Sinal:')
plt.title('Amplitude x Tempo')
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade')
plt.grid(True, linestyle ='-.')

###########################################################################
####### Gráfico da posição ##################
p = integrate.cumtrapz(v, t_cont, initial=0)  # Integrando usando a função cumptrapz

plt.figure()
plt.plot(t_cont, p, label = 'p', color = ('blue'), linewidth = 2)

####### Moldando o gráfico da posição ######
plt.legend(title='Sinal:')
plt.title('Amplitude x Tempo')
plt.xlabel('Tempo(s)')
plt.ylabel('Posição')
plt.grid(True, linestyle ='-.')

###########################################################################
####### Gráfico da referência x controlado ##
plt.figure()
posição, tposição , vposição = lsim(MalhaFechadaC, p, t_cont) # Usando lsim pra simular
plt.plot(t_cont, posição, label="Sistema controlado", color = ('blue'), linewidth = 2)
plt.plot(t_cont, p, label="Referência", color = ('red'), linewidth = 2)

####### Moldando o gráfico da posição ######
plt.legend(title='Sinal:')
plt.title('Amplitude x Tempo')
plt.xlabel('Tempo(s)')
plt.ylabel('Posição')
plt.grid(True, linestyle ='-.')

###########################################################################
Ka = posição[-1]-p[-1]   # Verificando erro
if Ka < 0.01:
    print("\nKa está OK. Ka =", Ka)
else:
    print("\n Erro maior que o limite. Ka = ", Ka)

###########################################################################
###### Aplicando degrau de 0.05 ############
plt.figure()
velocidade, tvelocidade, vvelelocidade = lsim(MalhaFechadaC*s, t_cont*0.05, t_cont) 
plt.plot(tvelocidade, velocidade, label="Velocidade", color = ('blue'), linewidth = 2)

####### Moldando o gráfico da posição ######
plt.legend(title='Sinal:')
plt.title('Amplitude x Tempo')
plt.xlabel('Tempo(s)')
plt.ylabel('Velocidade')
plt.grid(True, linestyle ='-.')

##########################################################################
####### Gráfico continuo x discreto ######################
pds, t_ds, vds = lsim(MalhaFechadaD, p, t_cont)
plt.figure()
plt.plot(t_cont, p, label="Sinal Contínuo", color = ('blue'), linewidth = 2)
plt.step(t_ds, pds,  label="Sinal Discreto", color = ('red'), linewidth = 2)

####### Moldando o gráfico da posição ######
plt.legend(title='Sinal:')
plt.title('Amplitude x Tempo')
plt.xlabel('Tempo(s)')
plt.ylabel('Posição')
plt.grid(True, linestyle ='-.')

plt.show()


