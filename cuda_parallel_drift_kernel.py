import numpy as np
from numba import cuda, uint64

# Kernel de CUDA
@cuda.jit
def collatz_analysis_kernel(start_n, steps_arr, drift_arr):
    # Identificador único del hilo
    idx = cuda.grid(1)
    
    if idx < len(steps_arr):
        n = start_n + idx
        initial_bits = 0
        
        # Contar bits iniciales (popcount)
        # Usamos una representación simple para este ejemplo
        temp_n = n
        while temp_n > 0:
            if temp_n & 1: initial_bits += 1
            temp_n >>= 1
            
        current = n
        steps = 0
        accum_bits = 0
        
        # Bucle de Collatz
        while current > 1 and steps < 5000:
            if current % 2 == 0:
                current //= 2
            else:
                current = (3 * current + 1) // 2
                steps += 1 # Compensación por la división integrada
            
            steps += 1
            
            # Medir densidad de bits en cada paso (opcional para lambda)
            # accum_bits += popcount(current) ...
            
        steps_arr[idx] = steps
        # Calculamos una derivada simple de bits (final - inicial) / pasos
        # Este es un esquema simplificado de tu 'lambda'
        drift_arr[idx] = current - n # Ejemplo de cambio de magnitud

def run_collatz_gpu(start, count):
    # Configuración de la GPU
    threads_per_block = 256
    blocks_per_grid = (count + (threads_per_block - 1)) // threads_per_block
    
    # Preparar arrays en la memoria de la GPU
    d_steps = cuda.device_array(count, dtype=np.int32)
    d_drift = cuda.device_array(count, dtype=np.float32)
    
    # Lanzar el kernel
    collatz_analysis_kernel[blocks_per_grid, threads_per_block](start, d_steps, d_drift)
    
    # Recuperar resultados
    return d_steps.copy_to_host(), d_drift.copy_to_host()

# Ejecución
inicio = 10**15
cantidad = 100000
pasos, deriva = run_collatz_gpu(inicio, cantidad)

print(f"Análisis completado para {cantidad} números.")
print(f"Promedio de pasos para n={inicio}: {np.mean(pasos)}")