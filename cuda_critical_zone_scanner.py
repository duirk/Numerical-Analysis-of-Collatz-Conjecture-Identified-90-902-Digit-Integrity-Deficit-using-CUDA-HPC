import torch

def buscar_zonas_criticas_cuda(rango_k=10000000):
    if not torch.cuda.is_available():
        print("CUDA no detectado. Usando CPU (será mucho más lento).")
        device = "cpu"
    else:
        device = "cuda"
        print(f"Usando GPU: {torch.cuda.get_device_name(0)}")

    # Generamos 10 millones de valores de k (pasos impares)
    k = torch.arange(1, rango_k, device=device, dtype=torch.float64)
    
    # Calculamos el L teórico que cancelaría la disipación (L = k * log2(3))
    log2_3 = 1.584962500721156
    L_teorico = k * log2_3
    
    # Tomamos los enteros más cercanos (pasos pares reales)
    L_real = torch.round(L_teorico)
    
    # Calculamos el error de aproximación (el "peligro" para tu tesis)
    error = torch.abs(L_real - L_teorico)
    
    # Buscamos los 5 casos más críticos en todo el rango
    valores_top, indices_top = torch.topk(error, k=5, largest=False)
    
    print("\n--- RESULTADOS DE LA BÚSQUEDA CUDA ---")
    for i in range(5):
        idx = indices_top[i].item()
        print(f"Candidato {i+1}: k={k[idx].item():.0f}, L={L_real[idx].item():.0f}")
        print(f"Precisión del balance: {valores_top[i].item():.12f}")

buscar_zonas_criticas_cuda()