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

######### QUESTÃO B ############

Ts = 0.03 #  Definindo período
g_s = tf(2098, [1, 74, 2098, 0]) # Definindo função de transferência
g_z = c2d(g_s, Ts, method='tustin') # Fazendo função de transferência discretizada usando o método de tustin
print(f"G(z): {g_z}") # Realizando print da função de transferência
