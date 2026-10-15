from sense_emu import SenseHat
import time

sense = SenseHat()
rouge = (255,0,0)

def clignotement(couleur, nb_fois=3, duree=0.3):
    for _ in range(nb_fois):
        sense.clear(couleur)
        time.sleep(duree)
        sense.clear()
        time.sleep(duree)

while True:
    if (sense.get_temperature() > 0):
        print("Temperature depassant 0")
        clignotement(rouge)

    time.sleep(0.1)


