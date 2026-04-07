import numpy as np
from numba import cuda
import math

@cuda.jit
def statistical_lambda_kernel(start_n, lambda_results):
    idx = cuda.grid(1)
    if idx < len(lambda_results):
        n_initial = float(start_n + idx)
        current = n_initial
        steps = 0
        log_initial = math.log(n_initial)
        
        while current > 1 and steps < 5000: # Aumentamos límite de pasos
            if current % 2 == 0:
                current /= 2
            else:
                current = (3 * current + 1) / 2
                steps += 1
            steps += 1
            
        if steps > 0:
            log_final = math.log(current)
            lambda_results[idx] = (log_final - log_initial) / steps
        else:
            lambda_results[idx] = 0

def analyze_extreme_cases(start, count):
    threads_per_block = 256
    blocks_per_grid = (count + (threads_per_block - 1)) // threads_per_block
    d_lambda = cuda.device_array(count, dtype=np.float32)
    
    statistical_lambda_kernel[blocks_per_grid, threads_per_block](start, d_lambda)
    
    h_lambda = d_lambda.copy_to_host()
    
    print(f"--- Análisis de Deriva (λ) para n={start} ---")
    print(f"Media (E[λ]):      {np.mean(h_lambda):.10f}")
    print(f"Máximo (Peor caso): {np.max(h_lambda):.10f}") 
    print(f"Mínimo (Mejor caso): {np.min(h_lambda):.10f}")
    print(f"Desviación Est.:    {np.std(h_lambda):.10f}")
    
    # Contar si algún número logró una deriva positiva
    positives = np.sum(h_lambda > 0)
    print(f"Números con deriva positiva: {positives}")

# Ejecutar análisis
analyze_extreme_cases(10**15, 100000)