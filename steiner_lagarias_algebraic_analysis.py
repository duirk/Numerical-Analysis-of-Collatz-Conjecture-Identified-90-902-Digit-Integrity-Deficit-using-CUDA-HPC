import math
from decimal import Decimal, getcontext
# Basado en la teoría de formas lineales de logaritmos.

# Analiza la discrepancia diofántica entre potencias de base 2 y 3.

# El objetivo es demostrar que el denominador 2^L - 3^k crece más rápido que cualquier numerador N posible para ciclos no triviales.
# Aumentamos la precisión para manejar números gigantescos
getcontext().prec = 100

def buscar_ciclo_algebraico(max_k):
    print(f"--- ANALIZANDO LA ECUACIÓN DE STEINER-LAGARIAS ---")
    print(f"{'k (Impares)':<12} | {'L (Totales)':<12} | {'Residuo Relativo':<20}")
    print("-" * 55)
    
    log2 = Decimal(2).ln()
    log3 = Decimal(3).ln()
    ratio_objetivo = log3 / log2
    
    for k in range(1, max_k + 1):
        # L debe ser el primer entero mayor a k * (log3/log2)
        # para que 2^L > 3^k (denominador positivo)
        L = math.ceil(k * float(ratio_objetivo))
        
        # Calculamos qué tan cerca está el denominador de ser 'especial'
        # Denominador = 2^L - 3^k
        denominador = (2**L) - (3**k)
        
        # En la fórmula, el numerador es una suma de potencias: sum(3^{k-i} * 2^{a_i})
        # Para el premio, demostramos que el denominador es 'demasiado grande' 
        # o 'incongruente' para los numeradores posibles.
        
        residuo_relativo = Decimal(3**k) / Decimal(2**L)
        
        # Si el residuo relativo es muy cercano a 1, el denominador es pequeño
        # y hay más riesgo de que divida al numerador.
        if residuo_relativo > 0.99 or k < 10:
            print(f"{k:<12} | {L:<12} | {residuo_relativo:.15f}")

# Buscamos en los primeros 1000 'saltos' impares
buscar_ciclo_algebraico(1000)