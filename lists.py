my_list = list()
my_other_list = []

#print(len(my_list))

my_list = [35, 25, 33, 22, 33]

#print(my_list)
#print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

#print(my_other_list)
#print(type(my_other_list))
#print(type(my_list))
"""print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[-1-2])
print(my_other_list[-2])
print(my_other_list[-4])"""
"""print(my_other_list.count("34"))"""
#age, height, name, surname = my_other_list
#print(name)

age, height, name, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
#print(name, surname)

"""print(my_list + my_other_list)

my_list = ["Hola Python"]
print(my_list)
print(type(my_list))"""

#my_other_list.append("Hello")
#print(my_other_list)

#my_other_list.insert(0,"Hello")
#print(my_other_list)

#my_list = "1","2"
#print(type(my_list))
'''my_tuple = "123"'''
"""print(my_tuple)
print(type(my_tuple))
print(my_tuple[2])
print(my_tuple.count("Brais"))
print(my_tuple.index(3))"""
#print(my_other_list.index("Brais"))
#my_tuple[1] = 1.8
#print(my_tuple[5])
#my_other_tuple = "Sol"

"""my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:5])"""
'''my_tuple = list(my_tuple)'''
#print(type(my_tuple))

#my_tuple[5] = "MoureDev"
#my_tuple.insert(0,"azul")
#print(tuple(my_tuple))

'''my_tuple = "Jose Perea Bueno"
my_other_tuple = list(" 25 años")
my_tuple = list(my_tuple)
my_tuple_2 = my_tuple[3]
my_tuple[3]= "Caca"
my_tuple_customized = my_tuple + my_tuple[3]
#print(my_tuple.index("e"))
print(my_tuple[3    ])'''

my_tuple = "Brais",1,2,3
my_tuple_2 = "Moure",2
my_total_tuple = (my_tuple + my_tuple_2)
#print(my_total_tuple[0:3])
my_tuple = list(my_tuple)
my_tuple[0] = "Polla"
my_tuple.insert(1, "azul")
print(tuple(my_tuple))
print(type(my_tuple))

del my_tuple

