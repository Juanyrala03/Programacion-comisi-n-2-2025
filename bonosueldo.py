
print("CALCULADORA DE SUELDO CON BONUS")

nombre = input("ingrese su nombre y apellido:")
sueldo = float(input("Ingrese su sueldo base:"))
bono= float(input("¿Cuál es su monto de bono deseado?:"))

Sueldo_final = sueldo + sueldo * bono

print(nombre,"el sueldo total correspondiente es de", Sueldo_final)