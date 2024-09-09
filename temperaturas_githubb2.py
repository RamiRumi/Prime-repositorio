import random

def crear_matriz_temperaturas(ciudades, dias, semanas):
    return [[[random.randint(15, 35) for _ in range(dias)] for _ in range(semanas)] for _ in range(ciudades)]

def calcular_promedio_semanal(temperaturas_semanales):
    return sum(temperaturas_semanales) / len(temperaturas_semanales)

# Configuración
ciudades = ['Machala', 'Naranjal', 'Guayaquil', 'Santa Elena']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
num_semanas = 2

# Crear matriz de temperaturas
temperaturas = crear_matriz_temperaturas(len(ciudades), len(dias_semana), num_semanas)

# Calcular y mostrar promedios
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura para {ciudad}:")
    for semana in range(num_semanas):
        promedio = calcular_promedio_semanal(temperaturas[ciudad_idx][semana])
        print(f"Semana {semana + 1}: {promedio:.2f}°C")

# matriz deverificación
print("\nMatriz completa de temperaturas:")
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for semana in range(num_semanas):
        print(f"Semana {semana + 1}:")
        for dia_idx, dia in enumerate(dias_semana):
            temp = temperaturas[ciudad_idx][semana][dia_idx]
            print(f"  {dia}: {temp}°C")