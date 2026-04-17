import datetime
import calendar
from  europeos import comprobar_signo_tropical, comprobar_signo_sideral, comprobar_signo_druidico

def pedir_entero(mensaje, min, max):
    while True:
        try:
            valor = int(input(mensaje))
            if min <= valor <= max:
                return valor
            else:
                print(f"El valor debe estar entre {min} y {max}.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

def validar_fecha_detallada(dia, mes, anyo):
    if mes < 1 or mes > 12:
        return False, f"El mes {mes} no es válido. Debe estar entre 1 y 12."

    dias_en_mes = calendar.monthrange(anyo, mes)[1]

    if dia < 1 or dia > dias_en_mes:
        return False, f"El día {dia} no es válido para el mes de {calendar.month_name[mes]} del año {anyo}. " \
                      f"(Ese mes tiene {dias_en_mes} días)."

    return True, ""

def pedir_fecha():
    while True:
        dia = pedir_entero("Introduce el día de nacimiento (1-31): ", 1, 31)
        mes = pedir_entero("Introduce el mes de nacimiento (1-12): ", 1, 12)
        anyo = pedir_entero("Introduce el año de nacimiento (1900-2026): ", 1900, 2026)

        valida, mensaje = validar_fecha_detallada(dia, mes, anyo)

        if valida:
            return datetime.date(anyo, mes, dia)
        else:
            print(f"\nLa fecha introducida no es valida: {mensaje}\nRevise los datos e inténtalo de nuevo.\n")


def main():
    print("Bienvenido a zodiacally.")
    fecha_nacimiento = pedir_fecha()

    tipo_zodiaco = input("¿Qué tipo de zodiaco quieres consultar? (tropical/sideral/druidico/todos): ").strip().lower()
    while tipo_zodiaco not in ["tropical", "sideral", "druidico", "todos"]:
        print("Opción no válida. Por favor, elige entre 'tropical', 'sideral', 'druidico' o 'todos'.")
        tipo_zodiaco = input("¿Qué tipo de zodiaco quieres consultar? (tropical/sideral/druidico/todos): ").strip().lower()

    print(f"\nHas nacido el {fecha_nacimiento.strftime('%d/%m/%Y')}.")

    if tipo_zodiaco == "tropical":
        signo = comprobar_signo_tropical(fecha_nacimiento.day, fecha_nacimiento.month)
        print(f"Tu signo zodiacal occidental es: {signo}")
    elif tipo_zodiaco == "sideral":
        signo = comprobar_signo_sideral(fecha_nacimiento.day, fecha_nacimiento.month)
        print(f"Tu signo zodiacal sideral es: {signo}")
    elif tipo_zodiaco == "druidico":
        signo = comprobar_signo_druidico(fecha_nacimiento.day, fecha_nacimiento.month)
        print(f"Tu signo zodiacal druídico es: {signo}")

    elif tipo_zodiaco == "todos":
        signo_tropical = comprobar_signo_tropical(fecha_nacimiento.day, fecha_nacimiento.month)
        signo_sideral = comprobar_signo_sideral(fecha_nacimiento.day, fecha_nacimiento.month)
        signo_druidico = comprobar_signo_druidico(fecha_nacimiento.day, fecha_nacimiento.month)

        print(f"Tu signo zodiacal occidental es: {signo_tropical}")
        print(f"Tu signo zodiacal sideral es: {signo_sideral}")
        print(f"Tu signo zodiacal druídico es: {signo_druidico}")
    else:
        print("Opción no válida. No se pudo determinar el signo zodiacal.")

if __name__ == "__main__":
    main()
