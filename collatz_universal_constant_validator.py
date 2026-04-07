import random

def escaneo_universal_desintegracion(bits, muestras):
    print(f"--- VALIDACIÓN UNIVERSAL DE DESINTEGRACIÓN (2^{bits}) ---")
    print(f"{'Muestra':<8} | {'Pasos':<10} | {'V. Desintegración':<18} | {'Estado'}")
    print("-" * 65)
    
    velocidades = []

    for i in range(1, muestras + 1):
        # Generamos un número aleatorio de alta energía
        n = random.getrandbits(bits) | (1 << (bits - 1)) | 1
        densidad_inicial = bin(n).count('1') / bits
        pasos = 0
        n_inicio = n
        
        # Buscamos el punto de equilibrio (0.55)
        while n > 1:
            if n % 2 == 0:
                n >>= 1
            else:
                n = 3 * n + 1
            pasos += 1
            
            # Chequeo de densidad cada 500 pasos para eficiencia
            if pasos % 500 == 0:
                bin_n = bin(n)[2:]
                densidad_actual = bin_n.count('1') / len(bin_n)
                if densidad_actual <= 0.55:
                    v = (densidad_inicial - densidad_actual) / pasos
                    velocidades.append(v)
                    print(f"#{i:<7} | {pasos:<10} | {v:.8f}        | VALIDADO")
                    break
        
    v_promedio = sum(velocidades) / len(velocidades)
    print("-" * 65)
    print(f"CONSTANTE UNIVERSAL DE COLATZ (λ): {v_promedio:.8f}")
    return v_promedio

# Ejecutamos la validación final
escaneo_universal_desintegracion(50000, 10)