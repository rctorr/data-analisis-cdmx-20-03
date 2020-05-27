linea = "-" * 60
formato1 = "{:15} | {:15} | {:10}"  # Formato para encabezado
formato2 = "{:15} | {:15} | {:>10}"  # Formato para recorridos
formato3 = "{:15} | {:>15} | {:>10}"  # Formato para total

print()
print(linea)
print(formato1.format("ORIGEN", "DESTINO", "TIEMPO"))
print(linea)
print(formato2.format("Roma Norte", "Tabacalera", "15:00"))
print(formato2.format("Reforma", "Juárez", "8:00"))
print(formato2.format("Alameda", "Condesa", "20:00"))
print(formato2.format("Roma Sur", "Roma Norte", "4:00"))
print(formato2.format("Buenavista", "Del Valle Norte", "30:00"))
print(linea)
print(formato3.format("", "Tiempo total:", "1:17:00"))
print()