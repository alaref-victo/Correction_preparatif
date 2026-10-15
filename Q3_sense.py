from sense_emu import SenseHat
import time

sense = SenseHat()

# position initial
x = 0
y = 0


def dessiner(x, y):
    sense.clear()
    sense.set_pixel(x, y, (255,255,255))


# Dans nos coordonne le y va venir avant le x et il y a une inversion
# par rapport a un plan cartesien
def deplacement(direction, x, y):

    if direction == "up":
        y -= 1
    elif direction == "down":
        y += 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1

    x = max(0, min(7, x))
    y = max(0, min(7, y))

    return x, y




dessiner(x, y)
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction in ("up", "down", "left", "right"):
                x, y = deplacement(event.direction, x, y)
                dessiner(x, y)
    time.sleep(0.05)