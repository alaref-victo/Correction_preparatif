# Note : attention avec les ranges

# La maniere classique

a = []

for i in range(0,100):
    if i % 2 == 0:
        a.append(i)

print("a :", a)


# La maniere pythonique
b = [i for i in range (0,100) if i % 2 == 0]
print("b :", b)

