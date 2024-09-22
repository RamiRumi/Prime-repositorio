# Crear función/es para calcular el total de un item en un factura, guardar los items en una matriz
# y mostrar el total de la factura

def calculo_valor_item(producto, cantidad, precio_unitario):
    subtotal = cantidad * precio_unitario
    matriz_item = [producto, cantidad, precio_unitario, subtotal]
    return matriz_item

def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

matriz_factura = []
matriz_factura.append(calculo_valor_item(producto="FIDEOS", cantidad=1, precio_unitario=0.60))
matriz_factura.append(calculo_valor_item(producto="PAPAS", cantidad=2, precio_unitario=1.10))
matriz_factura.append(calculo_valor_item(producto="ARROZ", cantidad=1, precio_unitario=0.60))

print("Factura original:")
print(matriz_factura)

# Calcular el total de la factura
total_factura = sum(item[3] for item in matriz_factura)

# Llamar a la función calcular_descuento dos veces
descuento1 = calcular_descuento(total_factura)
descuento2 = calcular_descuento(total_factura, 15)

# Resultados
print(f"\nTotal de la factura: ${total_factura:.2f}")
print(f"Descuento del 10%: ${descuento1:.2f}")
print(f"Monto a pagar después del descuento del 10%: ${total_factura - descuento1:.2f}")

print(f"\nDescuento del 15%: ${descuento2:.2f}")
print(f"Monto a pagar después del descuento del 15%: ${total_factura - descuento2:.2f}")