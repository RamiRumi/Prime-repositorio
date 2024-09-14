def calcular_temperatura_promedio(datos_temperaturas):
    promedios = {}
    
    for ciudad, temperaturas in datos_temperaturas.items():
        # Calcula el promedio de temperaturas para cada ciudad
        promedio = sum(temperaturas) / len(temperaturas)
        # Redondea el resultado a dos decimales
        promedios[ciudad] = round(promedio, 2)
    
    return promedios

# imprimir resultados
def imprimir_resultados(datos, resultados):
    print("Datos de entrada:")
    for ciudad, temps in datos.items():
        print(f"{ciudad}: {temps}")
    print("\nTemperaturas promedio por ciudad:")
    for ciudad, promedio in resultados.items():
        print(f"{ciudad}: {promedio}°C")
    print("\n")

# Ciudades con temperaturas 
datos_ciudades = {
    "Machala": [23.43, 26.86, 25.86, 21.86],
    "Naranjal": [26.57, 26.14, 21.86, 25.14],
    "Guayaquil": [24.14, 29, 18.86, 20.71],
    "Santa Elena": [23.57, 25.71, 28.14, 27.29]
}

resultado = calcular_temperatura_promedio(datos_ciudades)
imprimir_resultados(datos_ciudades, resultado)


