import numpy as np
from numba import cuda
import math

@cuda.jit
def find_worst_case_kernel(start_n, lambda_results):
    idx = cuda.grid(1)
    if idx < len(lambda_results):
        n_initial = float(start_n + idx)
        current = n_initial
        steps = 0
        log_initial = math.log(n_initial)
        
        # Simulamos la trayectoria
        while current > 1 and steps < 10000:
            if current % 2 == 0:
                current /= 2
            else:
                current = (3 * current + 1) / 2
                steps += 1
            steps += 1
            
        if steps > 0:
            log_final = math.log(current)
            # Guardamos la deriva logarítmica
            lambda_results[idx] = (log_final - log_initial) / steps
        else:
            lambda_results[idx] = -999.0 # Caso trivial

def run_deep_analysis(start, count):
    threads_per_block = 256
    blocks_per_grid = (count + (threads_per_block - 1)) // threads_per_block
    d_lambda = cuda.device_array(count, dtype=np.float32)
    
    find_worst_case_kernel[blocks_per_grid, threads_per_block](start, d_lambda)
    h_lambda = d_lambda.copy_to_host()
    
    # Encontrar el índice del peor caso (el máximo lambda)
    worst_idx = np.argmax(h_lambda)
    worst_val = start + worst_idx
    worst_lambda = h_lambda[worst_idx]
    
    print(f"--- RESULTADOS DEL ANÁLISIS DE RESISTENCIA ---")
    print(f"Rango analizado: [{start} - {start + count}]")
    print(f"Peor número encontrado: {worst_val}")
    print(f"Lambda del peor número: {worst_lambda:.10f}")
    print(f"Margen hasta la supervivencia (λ=0): {abs(worst_lambda):.10f}")
    
    return worst_val, worst_lambda

# Ejecutar para n=10^15
peor_n, peor_l = run_deep_analysis(10**15, 100000)