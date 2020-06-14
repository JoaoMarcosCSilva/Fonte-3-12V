# CONFIGURAÇÃO

# Tensão máxima e mínima da fonte
V_max = 12
V_min = 3

# Queda de tensão (positiva) entre a base e o emissor do transistor
V_be = 714.612e-3

# Resistência do resistor depois do potenciômetro
Rb = 2000

# Corrente passando pela base do transistor (deveria ser exatamente 1ma, mas no falstad dá esse valor aí)
iB = 249.377e-6

# Tensão mínima garantida pelo capacitor
Vc = 18

# Tensão de quebra do diodo zener
Vz = 13


def get_Ra(V, R, Rb, x = 0):
    return (Rb + R - x)*(Vz - V)/(V + iB*Rb + iB*R - iB*x) - x

def get_R(V, Rb):
    return get_Ra(V, 0, Rb, 0)

def get_irb(V, Rb, R, x):
    return V/(Rb + x)

def get_ira(irb, iB):
    return irb + iB

def get_iz(Vc, Vz, Rz, ira):
    return (Vc - Vz)/Rz - ira

def get_max_Rz(Vc, Vz, ira, iz):
    return (Vc - Vz)/(ira + iz)

def get_P_Rz(Vc, Vz, ira, iz):
    return (Vc - Vz)*(ira + iz)

V_max += V_be
V_min += V_be
R_tot = get_R(V_min, Rb)
Ra = get_Ra(V_max, R_tot, Rb)
R = R_tot - Ra

irb_min = get_irb(V_min, Rb, R, 0)
irb_max = get_irb(V_max, Rb, R, R)

ira_min = get_ira(irb_min, iB)
ira_max = get_ira(irb_max, iB)

#iz_min = get_iz(Vc, Vz, Rz, ira_max)
#iz_max = get_iz(Vc, Vz, Rz, ira_min)

Rz_min = get_max_Rz(Vc, Vz, ira_max, 0)
Rz_max = get_max_Rz(Vc, Vz, ira_min, 0)

P_Rz_min = get_P_Rz(Vc, Vz, ira_min, 0)
P_Rz_max = get_P_Rz(Vc, Vz, ira_max, 0)

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