from math import sqrt

# CONFIGURAÇÃO

# Tensão máxima e mínima da fonte
V_max = 12
V_min = 3

# Queda de tensão (positiva) entre a base e o emissor do transistor
V_be = 1.292

# Resistência do resistor depois do potenciômetro
R_after = 4300

# Corrente passando pela base do transistor (deveria ser exatamente 1ma, mas no falstad dá esse valor aí)
iB = 2.475e-6

# Tensão mínima garantida pelo capacitor
Vc = 19

# Tensão de quebra do diodo zener
Vz = 15


# Calcula a corrente passando por um resistor
#=================================================
#
#               +---------+                     
#      V+-------+    R    +------+0V
#               +---------+
#
#=================================================
def current(V, R):
    return V / R

# Calcula R_before dados Vz, V_medium, R_after e Ib
# No circuito final, R_before corresponde à soma das resistências do potenciômetro e do resistor anterior a ele
#=======================================================================
#
#                                                   Ib
#                                                  +-->
#                                              +--------------
#                                              |
#                                              |
#                  +----------+                |  +---------+
#        Vz+-------+ R_before +--+ V_medium +--+--+ R_after +---------+0V
#                  +----------+                   +---------+
#
#=======================================================================
def total_R_before(V_medium, R_after, iB, Vz):
    total_current = current(V_medium, R_after) + iB
    R_before = (Vz - V_medium)/total_current
    return R_before

# Calcula R_A dados Vz, V_medium, R_after, Ib e R_before
# Esse passo efetivamente divide o resistor R_before do circuito anterior em dois resistores: o potenciômetro (R_pot) e o resistor anterior a ele (Ra)
#=======================================================================
#
#                  +----------+
#        Vz+-------+ R_before +--+
#                  +----------+
#
#   === === === === === === === === === === ===
#
#                  +--+  +----+
#        Vz+-------+Ra+--+Rpot+--+
#                  +--+  +----+
#
#=======================================================================
def get_resistances(V_min, V_max, R_after, iB, Vz):
    R_before = total_R_before(V_min, R_after, iB, Vz)

    a = iB
    b = (-1)*(Vz + iB*(R_after + R_before))
    c = (Vz - V_max)*(R_after + R_before)

    delta = b*b - 4*a*c
    
    resistencia = (-b - sqrt(delta))/(2*a)
    return resistencia, R_before - resistencia

# Adiciona a queda de tensão nos transistores às tensões desejadas, para compensar essa queda
V_max += V_be
V_min += V_be

# Calcula as resistências finais
Ra, Rpot = get_resistances(V_min, V_max, R_after, iB, Vz)
print("Potenciômetro:", Rpot)
print("Resistor à esquerda:", Ra)

# Calcula a corrente máxima que poderá passar pelo resistor à esquerda do Potenciômetro
max_current_Ra = current(V_max, Rpot + R_after) + iB

# Com esse valor, calcula a resistência máxima do resistor acima do diodo zener
R_zener = (Vc - Vz)/max_current_Ra
print("Resistor acima do zener:", R_zener)