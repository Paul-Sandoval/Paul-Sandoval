#Banco del Pichincha
# Solicitar información al usuario
print("Bienvenido al Banco del Pichincha")
print("Por favor ingrese sus datos")
nombre = input("Ingrese su nombre: ")
tipo_tarjeta = int(input("Ingrese el tipo de tarjeta\n -tipo 1\n -tipo 2\n -tipo 3\n -otro: "))
credito = float(input("Ingrese su crédito actual: "))

match (tipo_tarjeta):
    case 1:
        credito_nuevo= credito*1.25
        print(f"Estimado cliente su nuevo limite de credito es: {credito_nuevo}")
    case 2:
        credito_nuevo= credito*1.35
        print(f"Estimado cliente su nuevo limite de credito es: {credito_nuevo}")
    case 3:
        credito_nuevo= credito*1.4
        print(f"Estimado cliente su nuevo limite de credito es: {credito_nuevo}")
    case _:
        credito_nuevo= credito*1.5
        print(f"Estimado cliente sui nuevo limite de credito es: {credito_nuevo}")