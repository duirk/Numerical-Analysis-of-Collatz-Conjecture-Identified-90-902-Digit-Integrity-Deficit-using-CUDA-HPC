import time

def calcular_velocidad_desintegracion(bits_objetivo):
    # Creamos un número de máxima densidad (todo unos)
    n = (1 << bits_objetivo) - 1
    densidad_inicial = 1.0
    pasos = 0
    
    print(f"--- MIDIENDO DEGRADACIÓN DE 2^{bits_objetivo}-1 ---")
    
    # El "Estado de Equilibrio" es 0.5 (caos total)
    while n > 1:
        bin_n = bin(n)[2:]
        densidad_actual = bin_n.count('1') / len(bin_n)
        
        # Si llegamos cerca del caos (0.5), hemos ganado
        if densidad_actual <= 0.55:
            print(f"¡Equilibrio alcanzado en el paso {pasos}!")
            print(f"Densidad final: {densidad_actual:.4f}")
            print(f"Velocidad de desintegración: {(1.0 - densidad_actual)/pasos:.6f} delta/paso")
            return pasos
        
        if n % 2 == 0:
            n >>= 1
        else:
            n = 3 * n + 1
        pasos += 1
        
        if pasos % 1000 == 0:
            print(f"Paso {pasos}: Densidad aún en {densidad_actual:.4f}...")

# Probamos con un bloque masivo de 50,000 bits
calcular_velocidad_desintegracion(50000)