import numpy as np
from numba import cuda
import math

@cuda.jit
def lambda_analysis_kernel(start_n, lambda_results):
    idx = cuda.grid(1)
    if idx < len(lambda_results):
        n_initial = float(start_n + idx)
        current = n_initial
        steps = 0
        
        # Registramos el logaritmo inicial
        log_initial = math.log(n_initial)
        
        while current > 1 and steps < 2000:
            if current % 2 == 0:
                current /= 2
            else:
                current = (3 * current + 1) / 2
                steps += 1
            steps += 1
            
        # Al final, calculamos la diferencia logarítmica por paso
        if steps > 0:
            log_final = math.log(current)
            # lambda = (log_final - log_initial) / pasos
            lambda_results[idx] = (log_final - log_initial) / steps
        else:
            lambda_results[idx] = 0

def calculate_lambda(start, count):
    threads_per_block = 256
    blocks_per_grid = (count + (threads_per_block - 1)) // threads_per_block
    
    d_lambda = cuda.device_array(count, dtype=np.float32)
    lambda_analysis_kernel[blocks_per_grid, threads_per_block](start, d_lambda)
    
    return d_lambda.copy_to_host()

# Prueba con  100,000 números
start_val = 10**15
lambdas = calculate_lambda(start_val, 100000)

print(f"Valor esperado de lambda (E[λ]): {np.mean(lambdas):.10f}")