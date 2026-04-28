def _fecha_en_rango(dia, mes, inicio, fin):
    mes_ini, dia_ini = inicio
    mes_fin, dia_fin = fin

    fecha = (mes, dia)
    return (mes_ini, dia_ini) <= fecha <= (mes_fin, dia_fin)

def comprobar_signo(dia, mes, tabla):
    """Función genérica que busca el signo en la tabla dada."""
    for signo, inicio, fin in tabla:
        if inicio[0] > fin[0]:
            if _fecha_en_rango(dia, mes, inicio, (12, 31)) or \
               _fecha_en_rango(dia, mes, (1, 1), fin):
                return signo
        else:
            if _fecha_en_rango(dia, mes, inicio, fin):
                return signo
    return "Desconocido"