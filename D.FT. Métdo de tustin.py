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

######### QUESTÃO F ############

Ts = 0.03 #  Definindo período
c_s = tf([7.0482, 6.38989812], [1, 0]) # Definindo função de transferência
c_z = c2d(c_s, Ts, method='tustin') # Fazendo função de transferência discretizada usando o método de tustin
print(f"C(z): {c_z}") # Realizando print da função de transferência