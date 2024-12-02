"""
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
if my_condition == 10:
    print("Es igual a 10")

else:
    print("La ejecución continua")
"""
"""
my_string = "Mi cadena de textoo"

if my_string:
    print("Mi cadena de texto no es vacía")

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoo":
    print("Mi cadena de texto coinciden")

"""

my_condition = 0

"""while my_condition < 10:
    print(my_condition)
    my_condition += 2

else:
    print("Mi condición es mayor o igual que 10")

print("La ejecución continua")"""

my_condition = 1

while my_condition < 20:
    my_condition += 1
    print("Sí")
    if my_condition == 15:
        print("Mi condición es 15")
        break
        print(my_condition)

#For

my_list = [1,2,3,4,5,6,7,8,9,10]

for element in my_list:
    print(element)

my_tuple = (35,1.88,"Jose","Perea","Bueno")

my_set = {"Brais","Moure",35}

my_dict = {"Nombre":"Jose", "Apellido":"Perea", "Edad":26}
"""
for element in my_tuple:
    print(element)

for element in my_set:
    print(element)
"""
#for element in list(my_dict.values()):
#    print(element)

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("se ejecuta")
else:
    print("El bucle ha finalizado")