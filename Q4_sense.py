# A -30 deg : (0,0,255)
# A 105 deg : (255,0,0)
from time import sleep
from sense_emu import SenseHat

sense = SenseHat()


TEMP_MIN = -30 
TEMP_MAX = 105

echelle = 255 / (TEMP_MAX - TEMP_MIN) 


while True:
    temp = sense.get_temperature()
    r = int((temp - TEMP_MIN) * echelle)
    b = int((TEMP_MAX - temp) * echelle)
    print(r, b)

    sense.clear((r,0,b))

    sleep(0.01)