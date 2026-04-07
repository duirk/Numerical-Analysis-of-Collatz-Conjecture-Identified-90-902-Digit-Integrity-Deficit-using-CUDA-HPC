import numpy as np
import matplotlib.pyplot as plt
import math
#Nuevo Marco de Análisis de Desintegración de Bits
def analyze_worst_case_trajectory(n_initial):
    current = n_initial
    trajectory = [current]
    densities = []
    lambdas = []
    
    # Función para calcular densidad de bits (unos / total de bits)
    get_density = lambda x: bin(x).count('1') / (len(bin(x)) - 2)
    
    steps = 0
    log_initial = math.log(n_initial)
    
    while current > 1 and steps < 500:
        densities.append(get_density(current))
        
        if current % 2 == 0:
            current //= 2
        else:
            current = (3 * current + 1) // 2
        
        steps += 1
        trajectory.append(current)
        
        # Lambda instantáneo desde el inicio hasta el paso actual
        lambdas.append((math.log(current) - log_initial) / steps)

    return trajectory, densities, lambdas

# Ejecutar para el número encontrado por la GPU
n_peor = 1000000000006895
traj, dens, lambs = analyze_worst_case_trajectory(n_peor)

# Visualización de la "Desintegración"
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Pasos (Steps)')
ax1.set_ylabel('Densidad de Bits (ρ)', color='tab:blue')
ax1.plot(dens, color='tab:blue', label='Densidad de Bits', alpha=0.8)
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Deriva Logarítmica (λ)', color='tab:red')
ax2.plot(lambs, color='tab:red', linestyle='--', label='Evolución de λ')
ax2.axhline(y=0, color='black', linewidth=1) # Línea de supervivencia
ax2.tick_params(axis='y', labelcolor='tab:red')

plt.title(f'Análisis de Desintegración: n = {n_peor}')
fig.tight_layout()
plt.show()