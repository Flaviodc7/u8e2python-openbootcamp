class Vehiculo:
    ruedas = 4
    motor = 1
    velocidad = 180

coche = Vehiculo()

def guardarCoche():
    f = open('texto.txt', 'w')
    f.write(f'ruedas: {coche.ruedas}\nmotor: {coche.motor}\nvelocidad: {coche.velocidad}')
    f.close()

def leerTexto():
    f = open('texto.txt', 'r')
    print(f.read())
    f.close()

guardarCoche()
leerTexto()