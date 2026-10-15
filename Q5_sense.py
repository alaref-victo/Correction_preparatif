from sense_emu import SenseHat
import time

sense = SenseHat()

FICHIER = "Meteo.csv"


# on veut un format csv
with open(FICHIER, "w") as f:
    f.write("temps;temperature;humidite;pression\n")

while True:
    temps = time.time()
    temperature = sense.get_temperature()
    hum = sense.get_humidity()
    pres = sense.get_pressure()

    
    with open(FICHIER, "a") as f:
        f.write(str(temps) + ";" + str(temperature) + ";" + str(hum) + ";" + str(pres) + "\n")

    time.sleep(10)