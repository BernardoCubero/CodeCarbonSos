import time
import os
import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from codecarbon import EmissionsTracker

# Cargar el token desde el archivo .env
load_dotenv()
API_KEY = os.getenv("CODECARBON_API_KEY")

# Verificar si el token se cargó correctamente
if not API_KEY:
    raise ValueError("❌ El token CODECARBON_API_KEY no está configurado en el archivo .env.")

# Configurar el rastreador de emisiones
tracker = EmissionsTracker(
    project_name="CargaExtrema",
    api_call_interval=10,  # Enviar datos cada 10 segundos
    save_to_api=True,
    api_key=API_KEY,  # Asegurarse de pasar el token explícitamente
    output_file="emisiones_extremo.csv"
)

# Lista para almacenar emisiones en cada iteración
emisiones_lista = []

# Función para hacer cálculos pesados
def multiplicacion_matrices():
    A = np.random.rand(5000, 5000)  # Matriz grande 5000x5000
    B = np.random.rand(5000, 5000)
    _ = np.dot(A, B)  # Multiplicación de matrices

# Función para encontrar números primos grandes
def encontrar_primos(limite):
    primos = []
    for num in range(2, limite):
        es_primo = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if es_primo:
            primos.append(num)
    return primos

# Iniciar la medición de CO₂
tracker.start()

print("🚀 Ejecutando tareas intensivas en CPU y memoria (esto puede tardar)...")

# Usar múltiples hilos para tareas pesadas
with ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(5):  # Simulación de 5 iteraciones de carga extrema
        print(f"⚡ Iteración {i + 1} - Cargando CPU y RAM...")

        # Ejecutar tareas en paralelo
        executor.submit(multiplicacion_matrices)
        executor.submit(encontrar_primos, 5_000_000)

        # Esperar 3 segundos entre iteraciones
        time.sleep(3)

        # Obtener emisiones actuales después de detener el tracker
        try:
            emisiones_actuales = tracker.stop()  # Detener el tracker y obtener emisiones
            emisiones_lista.append(emisiones_actuales)
        except Exception as e:
            print(f"⚠️ Error al enviar datos al dashboard de CodeCarbon: {e}")

        # Reiniciar el tracker para continuar la medición
        tracker.start()

# Detener la medición final
tracker.stop()

# 📊 Graficar la evolución de emisiones
plt.plot(range(1, len(emisiones_lista) + 1), emisiones_lista, marker='o', linestyle='-', color='r')
plt.xlabel("Iteración")
plt.ylabel("Emisiones de CO₂ (kg)")
plt.title("Evolución de las emisiones de CO₂ en Carga Extrema")
plt.grid(True)
plt.show()

print("✅ Verifica tu cuenta en el CodeCarbon Dashboard para confirmar las métricas.")
