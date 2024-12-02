#numberOne, numberTwo = 1, 2
#print(numberOne, numberTwo)

numberOne = str("Comida"+"Food"+"Chicle")
numberTwo = str("Comida")
#numberTwo = "2"


"""if numberOne > 0:
    print(numberOne + numberTwo)
else:
    print("No se cumplió")"""

"""if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("No se cumplió")"""

try:
    print(numberOne + numberTwo)
    print("No hay error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continua correctamente")

finally:
    print("FInally")

print(numberOne + numberTwo)


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un error")
except ValueError:
    print("Se ha producido un error")
except ValueError as error:
    print(error)

