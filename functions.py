#def my_function ():
#    print("Esto es una función")
#
#my_function ()
"""my_function ()
my_function ()

def mi_funcion():
    print("Esta es mi fucking función")
mi_funcion()

def sum_two_values(first_value: int, second_value):
    
    print(first_value + second_value)

    
sum_two_values(2,3)

def sum_two_values_with_return(first_value,second_value):
    
    my_sum = first_value + second_value
    
    return my_sum

my_sum = sum_two_values_with_return(1.4, 5.2)
print(my_sum)

my_result = sum_two_values_with_return(10,5)
print(my_sum)
"""

"""def print_name(name,surname):
    print(f"{name} {surname}")

#print_name("Jose","Perea")
#print_name(surname = "Perea", name = "Jose")

def print_name_with_default (name, surname, alias = "| NO TIENE"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jose","Perea")
print_name_with_default("Jose","Perea","Alias")"""



def print_texts(*text):
    print(text)
    print(*text)

print_texts("hola","adiós") 

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Soy", "Brais")