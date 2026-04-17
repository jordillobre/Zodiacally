def comprobar_signo_tropical(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Aries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Tauro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Géminis"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Cáncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leo"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgo"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpio"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitario"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricornio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Acuario"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Piscis"

def comprobar_signo_sideral(dia, mes):
    if (mes == 4 and dia >= 14) or (mes == 5 and dia <= 14):
        return "Aries"
    elif (mes == 5 and dia >= 15) or (mes == 6 and dia <= 14):
        return "Tauro"
    elif (mes == 6 and dia >= 15) or (mes == 7 and dia <= 15):
        return "Géminis"
    elif (mes == 7 and dia >= 16) or (mes == 8 and dia <= 15):
        return "Cáncer"
    elif (mes == 8 and dia >= 16) or (mes == 9 and dia <= 15):
        return "Leo"
    elif (mes == 9 and dia >= 16) or (mes == 10 and dia <= 15):
        return "Virgo"
    elif (mes == 10 and dia >= 16) or (mes == 11 and dia <= 15):
        return "Libra"
    elif (mes == 11 and dia >= 16) or (mes == 12 and dia <= 15):
        return "Escorpio"
    elif (mes == 12 and dia >= 16) or (mes == 1 and dia <= 14):
        return "Sagitario"
    elif (mes == 1 and dia >= 15) or (mes == 2 and dia <= 14):
        return "Capricornio"
    elif (mes == 2 and dia >= 15) or (mes == 3 and dia <= 14):
        return "Acuario"
    elif (mes == 3 and dia >= 15) or (mes == 4 and dia <=13):
        return "Piscis"



def main():
    signo_tropical = comprobar_signo_tropical(6,4)
    signo_sideral = comprobar_signo_sideral(6,4)

    print(f"Tu signo zodiacal tropical es: {signo_tropical}")
    print(f"Tu signo zodiacal sideral es: {signo_sideral}")

if __name__ == "__main__":
    main()

