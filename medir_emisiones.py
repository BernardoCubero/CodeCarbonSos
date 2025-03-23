import time
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from codecarbon import EmissionsTracker

# Cargar el token desde el archivo .env
load_dotenv()
API_KEY = os.getenv("CODECARBON_API_KEY")

# Configurar el rastreador de emisiones con el API de CodeCarbon
tracker = EmissionsTracker(
    project_name="MiProyecto",
    api_call_interval=10,  # Enviar datos cada 10 segundos
    save_to_api=True
)

# Lista para almacenar emisiones
emisiones_lista = []

# Iniciar medición
tracker.start()

print("Ejecutando cálculos intensivos...")
for i in range(5):  # Simulación de 5 iteraciones
    sum([j**2 for j in range(10**6)])  # Cálculo pesado
    time.sleep(1)  # Simular procesamiento

    # Obtener emisiones actuales sin detener el tracker
    emisiones_actuales = tracker.stop()
    emisiones_lista.append(emisiones_actuales)

    # Reiniciar el tracker para continuar la medición
    tracker.start()

# Detener la medición
tracker.stop()

# 📊 Graficar las emisiones
plt.plot(range(1, len(emisiones_lista) + 1), emisiones_lista, marker='o', linestyle='-', color='b')
plt.xlabel("Iteración")
plt.ylabel("Emisiones de CO₂ (kg)")
plt.title("Evolución de las emisiones de CO₂")
plt.grid(True)
plt.show()

print("✅ Datos enviados a CodeCarbon Dashboard. Revisa tu cuenta para ver las métricas.")
