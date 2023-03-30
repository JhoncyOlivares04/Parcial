def calcular_precio_boletas():
    tipo_sala = input("¿Qué tipo de sala desea? (Dinamix, 3D o 2D): ")
    num_boletas = int(input("¿Cuántas boletas necesita?: "))
    hora_funcion = input("¿En qué hora desea la función? (formato: HH:MM AM/PM): ")
    medio_pago = input("¿Cuál es su medio de pago? (tarjeta_cinema u otro): ")
    reserva = input("¿Ha hecho reserva? (si o no): ")

    if tipo_sala == "Dinamix":
        tarifa_basica = 18800
    elif tipo_sala == "3D":
        tarifa_basica = 15500
    elif tipo_sala == "2D":
        tarifa_basica = 11300
    else:
        return "Tipo de sala inválido"

    hora_pico = False
    if hora_funcion.endswith("PM"):
        hora_pico = True

    descuento_hora_no_pico = 0
    if not hora_pico:
        descuento_hora_no_pico = 0.10

    descuento_num_boletas = 0
    if num_boletas >= 3:
        descuento_num_boletas = 0.5 * (num_boletas - 3)

    descuento_tarjeta_cinema = 0
    if medio_pago == "tarjeta_cinema":
        descuento_tarjeta_cinema = 0.05

    recargo_reserva = 0
    if reserva == "si":
        recargo_reserva = 2000

    tarifa_final = tarifa_basica * (1 + descuento_tarjeta_cinema - descuento_hora_no_pico) - descuento_num_boletas + recargo_reserva

    if hora_pico:
        if tipo_sala == "2D" or tipo_sala == "3D":
            tarifa_final *= 1.25
        elif tipo_sala == "Dinamix":
            tarifa_final *= 1.5

    return f"El precio total de las {num_boletas} boletas para la función en la sala {tipo_sala} a las {hora_funcion} es de {tarifa_final:.0f} pesos."


print(calcular_precio_boletas())

