#dict
my_dict_schedule={'Wake_up:': 08.00, 'Training:': 08.15, 'Breakfast:': 08.45}
print(my_dict_schedule)
print(my_dict_schedule['Wake_up:'])
print(my_dict_schedule.get('launch'))
my_dict_schedule['Wake_up:']=08.05 # replacement
my_dict_schedule['Have a shower']=23.15
my_dict_schedule['Dinner']=19.30
my_dict_schedule['Go to bed']=23.45
print(my_dict_schedule)
del my_dict_schedule['Go to bed']
print(my_dict_schedule)
my_dict_schedule.update({'Wake_up:': 07.00, 'Training:': 07.15, 'Breakfast:': 07.45})
print(my_dict_schedule)
#set
my_set={'size', 'type', 'model', 36, 36, 37, 37, 37, 39, 38, 38, 39, 40, 40}
print(my_set)
my_set.add('color')
my_set.add('season')
print(my_set)
my_set.remove(36)
print(my_set)
my_set.discard(40)
print(my_set)





