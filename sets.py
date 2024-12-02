'''my_set = set()

my_other_set = {}

print(type(my_set))
print(type(my_other_set))'''

my_other_set = {25,"Brais","Moure","Garcia","Perez",36}

'''print(my_other_set)
print(type(my_other_set))
print(len(my_other_set))
print(my_other_set[0])'''

my_other_set.add("Mouredev")
my_other_set.add("BArca")
my_other_set.add("Madrid")
#print(my_other_set)

'''print("Moure" in my_other_set)
print(my_other_set)
my_other_set.remove("Moure")
print(my_other_set)'''
#my_other_set.clear();print(len(my_other_set))
#del (my_other_set); print(my_other_set)

my_set = {"Brais","Moure",35}
my_list = list(my_set)
'''print(my_list)
print(my_list[1])'''

my_other_set = {"Kotlin","Swift","Python"}

my_new_set = my_set.union(my_other_set)

"""print(my_new_set)
print(my_new_set.union(my_new_set))"""
print(my_new_set.union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))

print(my_set.difference(my_new_set))

