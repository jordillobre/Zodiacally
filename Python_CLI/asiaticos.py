from utils import comprobar_signo

SIGNOS_VEDAS = [
    ("Mesha",       (4, 14), (5, 14)),
    ("Vrishabha",   (5, 15), (6, 14)),
    ("Mithuna",     (6, 15), (7, 14)),
    ("Karka",       (7, 15), (8, 14)),
    ("Simha",       (8, 15), (9, 15)),
    ("Kanya",       (9, 16), (10, 15)),
    ("Tula",        (10, 16), (11, 14)),
    ("Vrishchika",  (11, 15), (12, 14)),
    ("Dhanu",       (12, 15), (1, 13)),
    ("Makara",      (1, 14), (2, 11)),
    ("Kumbha",      (2, 12), (3, 12)),
    ("Meena",       (3, 13), (4, 13)),
]



def comprobar_signo_vedas(dia, mes):
    return comprobar_signo(dia, mes, SIGNOS_VEDAS)
