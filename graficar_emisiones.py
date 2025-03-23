import time
import matplotlib.pyplot as plt
from codecarbon import EmissionsTracker

# Lista para almacenar emisiones en cada iteración
emisiones_lista = []

# Crear el rastreador
tracker = EmissionsTracker()

# Iniciar medición
tracker.start()

print("Ejecutando cálculos intensivos...")
for i in range(5):  # Simulación de 5 iteraciones
    sum([j**2 for j in range(10**6)])  # Cálculo pesado
    time.sleep(1)  # Simular tiempo de cómputo

    # Obtener emisiones actuales sin detener el tracker
    emisiones_actuales = tracker.stop()
    emisiones_lista.append(emisiones_actuales)

    # Reiniciar el rastreador en cada iteración para acumular datos
    tracker.start()

# Detener el rastreador al final
tracker.stop()

tracker = EmissionsTracker(
    output_file="emisiones.csv",
    save_to_api=True
)

# 📊 Graficar las emisiones
plt.plot(range(1, len(emisiones_lista) + 1), emisiones_lista, marker='o', linestyle='-', color='b')
plt.xlabel("Iteración")
plt.ylabel("Emisiones de CO₂ (kg)")
plt.title("Evolución de las emisiones de CO₂")
plt.grid(True)
plt.show()
