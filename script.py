from math import sqrt

# CONFIGURAÇÃO

# Tensão máxima e mínima da fonte
V_max = 12.1
V_min = 2.8

# Queda de tensão (positiva) entre a base e o emissor do transistor
V_be = 1.292

# Resistência do resistor depois do potenciômetro
Rb = 4300

# Corrente passando pela base do transistor (deveria ser exatamente 1ma, mas no falstad dá esse valor aí)
iB = 2.475e-6

# Tensão mínima garantida pelo capacitor
Vc = 19

# Tensão de quebra do diodo zener
Vz = 14.9

def get_R(V, Rb):
    a = -iB
    b = V - iB*Rb
    c = Rb * (Vz - V)
    D = sqrt(b*b - 4*a*c)
    return -(-b + D)/(2*a)

def get_Ra(V, R):
    i = Vz/(R) + iB
    return (Vz - V)/i

def get_irb(V, Rb, R, x):
    return V/(Rb + x)

def get_ira(irb, iB):
    return irb + iB

def get_iz(Vc, Vz, Rz, ira):
    return (Vc - Vz)/Rz - ira

def get_max_Rz(Vc, Vz, ira):
    return (Vc - Vz)/(ira)

def get_P_Rz(Vc, Vz, ira):
    return (Vc - Vz)*(ira)

V_max += V_be
V_min += V_be
R_tot = get_R(V_min, Rb)
Ra = get_Ra(V_max, R_tot + Rb)
R = R_tot - Ra

irb_min = get_irb(V_min, Rb, R, 0)
irb_max = get_irb(V_max, Rb, R, R)

ira_min = get_ira(irb_min, iB)
ira_max = get_ira(irb_max, iB)

Rz_min = get_max_Rz(Vc, Vz, ira_max)
Rz_max = get_max_Rz(Vc, Vz, ira_min)

P_Rz_min = get_P_Rz(Vc, Vz, ira_min)
P_Rz_max = get_P_Rz(Vc, Vz, ira_max)

print('')
print('Resistência máxima do potenciômetro:', R)
print('')
print('Resistência do resistor antes do potenciômetro:', Ra)
print('')
print('Corrente mínima passando pelo resistor depois do potenciômetro', irb_min)
print('Corrente máxima passando pelo resistor depois do potenciômetro:', irb_max)
print('')
print('Corrente mínima passando pelo resistor antes do potenciômetro', ira_min)
print('Corrente máxima passando pelo resistor antes do potenciômetro:', ira_max)
print('')
print('Resistência mínima do resistor em cima do diodo zener:', Rz_min)
print('Resistência máxima do resistor em cima do diodo zener:', Rz_max)
print('')
print('Potência mínima do resistor em cima do diodo zener:', P_Rz_min)
print('Potência máxima do resistor em cima do diodo zener:', P_Rz_max)
