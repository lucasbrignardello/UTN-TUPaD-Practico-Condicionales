# Programa para determinar la estación del año según el hemisferio, mes y día

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Convertir la fecha a un número para facilitar la comparación (mes*100 + dia)
fecha = mes * 100 + dia

if hemisferio == "N":
    if (fecha >= 1221 and fecha <= 320):
        estacion = "Invierno"
    elif (fecha >= 321 and fecha <= 620):
        estacion = "Primavera"
    elif (fecha >= 621 and fecha <= 920):
        estacion = "Verano"
    elif (fecha >= 921 and fecha <= 1220):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if (fecha >= 1221 and fecha <= 320):
        estacion = "Verano"
    elif (fecha >= 321 and fecha <= 620):
        estacion = "Otoño"
    elif (fecha >= 621 and fecha <= 920):
        estacion = "Invierno"
    elif (fecha >= 921 and fecha <= 1220):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"

print("La estación del año es:", estacion)