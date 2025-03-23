import time
import os
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from codecarbon import EmissionsTracker

# Cargar el token desde el archivo .env
load_dotenv()
API_KEY = os.getenv("CODECARBON_API_KEY")

# Configurar el rastreador de emisiones con conexión al dashboard
tracker = EmissionsTracker(
    project_name="CargaPesada",
    api_call_interval=10,  # Enviar datos cada 10 segundos
    save_to_api=True,
    output_file="emisiones_pesado.csv"  # Guardar en CSV
)

# Lista para almacenar emisiones en cada iteración
emisiones_lista = []

# Iniciar la medición de CO₂
tracker.start()

print("🚀 Ejecutando cálculos de matrices grandes (Esto puede tardar)...")

for i in range(10):  # Simulación de 10 iteraciones de carga pesada
    print(f"⚡ Iteración {i + 1} - Cargando CPU...")
    
    # Crear y multiplicar matrices de gran tamaño
    A = np.random.rand(2000, 2000)  # Matriz 2000x2000
    B = np.random.rand(2000, 2000)  # Matriz 2000x2000
    C = np.dot(A, B)  # Multiplicación de matrices (carga pesada)

    # Simular un tiempo de espera (opcional)
    time.sleep(1)

    # Obtener emisiones actuales sin detener el tracker
    emisiones_actuales = tracker.stop()
    emisiones_lista.append(emisiones_actuales)

    # Reiniciar el tracker para continuar la medición
    tracker.start()

# Detener la medición final
tracker.stop()

# 📊 Graficar la evolución de emisiones
plt.plot(range(1, len(emisiones_lista) + 1), emisiones_lista, marker='o', linestyle='-', color='r')
plt.xlabel("Iteración")
plt.ylabel("Emisiones de CO₂ (kg)")
plt.title("Evolución de las emisiones de CO₂ en Cálculos Pesados")
plt.grid(True)
plt.show()

print("✅ Datos enviados a CodeCarbon Dashboard. Revisa tu cuenta para ver las métricas.")
