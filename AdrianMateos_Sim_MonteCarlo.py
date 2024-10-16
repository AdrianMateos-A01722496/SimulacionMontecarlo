import numpy as np

#Funcion 

def estimar_vida_util_satélite(n_experimentos, paneles, minimo, maximo):
    vida_total = 0  # Inicializar la variable para la vida total acumulada
    
    for _ in range(n_experimentos):
        # Simular la vida útil de los paneles (5 paneles, distribución uniforme)
        vidas_paneles = np.random.uniform(minimo, maximo, paneles)
        
        # Ordenar las vidas útiles de menor a mayor
        vidas_paneles_ordenadas = np.sort(vidas_paneles)
        
        # El segundo valor más grande es el momento en que han fallado 4 paneles
        # porque el último panel aún estaría en funcionamiento.
        vida_util = vidas_paneles_ordenadas[-2]
        
        # Acumular el tiempo de vida útil
        vida_total += vida_util
    
    # Estimar phi (vida útil esperada del satélite)
    phi_estimado = vida_total / n_experimentos
    
    return phi_estimado

#Parametros
NUM_SIMULACIONES = 10000
NUM_PANELES = 5
MINIMO = 1000
MAXIMO = 5000

estimacion_phi = estimar_vida_util_satélite(n_experimentos = NUM_SIMULACIONES,
                                            paneles = NUM_PANELES,
                                            minimo = MINIMO,
                                            maximo = MAXIMO)

print(f"Estimación de la vida útil del satélite (phi) despues de 10000 simulaciones: {estimacion_phi:.2f} horas")
