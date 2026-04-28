from utils import comprobar_signo

SIGNOS_TROPICAL = [
    ("Aries",      (3, 21), (4, 19)),
    ("Tauro",      (4, 20), (5, 20)),
    ("Géminis",    (5, 21), (6, 20)),
    ("Cáncer",     (6, 21), (7, 22)),
    ("Leo",        (7, 23), (8, 22)),
    ("Virgo",      (8, 23), (9, 22)),
    ("Libra",      (9, 23), (10, 22)),
    ("Escorpio",   (10, 23), (11, 21)),
    ("Sagitario",  (11, 22), (12, 21)),
    ("Capricornio",(12, 22), (1, 19)),
    ("Acuario",    (1, 20), (2, 18)),
    ("Piscis",     (2, 19), (3, 20)),
]

SIGNOS_SIDERAL = [
    ("Aries",      (4, 14), (5, 14)),
    ("Tauro",      (5, 15), (6, 14)),
    ("Géminis",    (6, 15), (7, 15)),
    ("Cáncer",     (7, 16), (8, 15)),
    ("Leo",        (8, 16), (9, 15)),
    ("Virgo",      (9, 16), (10, 15)),
    ("Libra",      (10, 16), (11, 15)),
    ("Escorpio",   (11, 16), (12, 15)),
    ("Sagitario",  (12, 16), (1, 14)),
    ("Capricornio",(1, 15), (2, 14)),
    ("Acuario",    (2, 15), (3, 14)),
    ("Piscis",     (3, 15), (4, 13)),
]

SIGNOS_DRUIDICOS = [
    ("Ciervo",              (12, 24), (1, 20)),
    ("Gato",                (1, 21), (2, 17)),
    ("Vibora",              (2, 18), (3, 17)),
    ("Zorro",               (3, 18), (4, 14)),
    ("Toro",                (4, 15), (5, 12)),
    ("Caballito de mar",    (5, 13), (6, 9)),
    ("Reyezuelo",           (6, 10), (7, 7)),
    ("Caballo",             (7, 8), (8, 4)),
    ("Salmón",              (8, 5), (9, 1)),
    ("Cisne",               (9, 2), (9, 29)),
    ("Mariposa",            (9, 30), (10, 27)),
    ("Lobo",                (10, 28), (11, 24)),
    ("Halcón",              (11, 25), (12, 23)),
]

SIGNOS_CELTA = [
    ("Ciervo",              (12, 24), (1, 20)),
    ("Gato",                (1, 21), (2, 17)),
    ("Vibora",              (2, 18), (3, 17)),
    ("Zorro",               (3, 18), (4, 14)),
    ("Toro",                (4, 15), (5, 12)),
    ("Caballito de mar",    (5, 13), (6, 9)),
    ("Reyezuelo",           (6, 10), (7, 7)),
    ("Caballo",             (7, 8), (8, 4)),
    ("Salmón",              (8, 5), (9, 1)),
    ("Cisne",               (9, 2), (9, 29)),
    ("Mariposa",            (9, 30), (10, 27)),
    ("Lobo",                (10, 28), (11, 24)),
    ("Halcón",              (11, 25), (12, 23)),
]

SIGNOS_RUNICO = [
    ("Fehu",        (6, 29), (7, 13)),
    ("Uruz",        (7, 14), (7, 28)),
    ("Thurisaz",    (7, 29), (8, 12)),
    ("Ansuz",       (8, 13), (8, 28)),
    ("Raidho",      (8, 29), (9, 12)),
    ("Kenaz",       (9, 13), (9, 27)),
    ("Gebo",        (9, 28), (10, 12)),
    ("Wunjo",       (10, 13), (10, 27)),
    ("Hagalaz",     (10, 28), (11, 12)),
    ("Nauthiz",     (11, 13), (11, 27)),
    ("Isa",         (11, 28), (12, 12)),
    ("Jera",        (12, 13), (12, 27)),
    ("Eihwaz",      (12, 28), (1, 12)),
    ("Perthro",     (1, 13), (1, 27)),
    ("Algiz",       (1, 28), (2, 12)),
    ("Sowilo",      (2, 13), (2, 26)),
    ("Tiwaz",       (2, 27), (3, 13)),
    ("Berkano",     (3, 14), (3, 29)),
    ("Ehwaz",       (3, 30), (4, 13)),
    ("Mannaz",      (4, 14), (4, 28)),
    ("Laguz",       (4, 29), (5, 13)),
    ("Ingwaz",      (5, 14), (5, 28)),
    ("Dagaz",       (5, 29), (6, 13)),
    ("Othala",      (6, 14), (6, 28)),
]

def comprobar_signo_tropical(dia, mes):
    return comprobar_signo(dia, mes, SIGNOS_TROPICAL)

def comprobar_signo_sideral(dia, mes):
    return comprobar_signo(dia, mes, SIGNOS_SIDERAL)

def comprobar_signo_druidico(dia, mes):
    return comprobar_signo(dia, mes, SIGNOS_DRUIDICOS)

def comprobar_signo_runico(dia, mes):
    return comprobar_signo(dia, mes, SIGNOS_RUNICO)