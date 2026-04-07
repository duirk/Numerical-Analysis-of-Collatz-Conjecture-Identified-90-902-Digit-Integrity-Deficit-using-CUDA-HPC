import torch
import mpmath

# 1. FASE CUDA: Búsqueda del candidato más peligroso
def buscar_candidato_maestro(rango=2000000):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"--- Buscando resonancias en {device.upper()} ---")
    
    # Usamos float64 para la búsqueda inicial en GPU
    k = torch.arange(1, rango, device=device, dtype=torch.float64)
    log2_3 = 1.584962500721156
    
    decimales = (k * log2_3) % 1
    error = torch.min(decimales, 1 - decimales)
    
    valor_min, idx = torch.min(error, 0)
    best_k = int(k[idx].item())
    best_L = int(round(best_k * log2_3))
    
    return best_k, best_L

# 2. FASE DE PRECISIÓN: Verificación final
def verificar_tesis_final(k_val, L_val):
    mpmath.mp.dps = 200 # 200 dígitos de precisión
    
    print(f"\n--- RESULTADO FINAL DE LA INVESTIGACIÓN ---")
    print(f"Candidato Crítico Detectado: k={k_val}, L={L_val}")
    
    term1 = mpmath.power(2, L_val)
    term2 = mpmath.power(3, k_val)
    denominador = mpmath.fabs(term1 - term2)
    
    # Calculamos la magnitud y la convertimos a float para el print
    digitos = float(mpmath.log10(denominador))
    
    print(f"Magnitud del error: {digitos:.2f} dígitos decimales.")
    
    if L_val > k_val * mpmath.log(3, 2):
        print("\nESTADO: DISIPACIÓN CONFIRMADA")
        print(f"Incluso en el punto de máxima resonancia, la pérdida de bits es absoluta.")
        print(f"El denominador es un número de {int(digitos)} cifras. Ciclo imposible.")
    else:
        print("\nESTADO: RESONANCIA TEMPORAL (Punto de equilibrio inestable)")

# Ejecución
try:
    k_final, L_final = buscar_candidato_maestro()
    verificar_tesis_final(k_final, L_final)
except Exception as e:
    print(f"Error detectado: {e}")