# def abc(**person):
#     # print(person)
#     ah = f"{person['a']} wrote this letter in {person['b']}"
#     return ah


# print(abc(a='Illia', b="LinkedIn", id=141))


# def abc(a, b):
#     ah = f"{a} wrote this letter in {b}"
#     return ah


# print(abc(a='Illia', b="LinkedIn"))


def merge_list_to_dict(a, b):
    c = zip(a, b)
    return dict(c)


print(merge_list_to_dict(a=['a', 'b', 'c'], b=[131, 133, 54354]))


print(merge_list_to_dict(['a', 'b', 'c'], b=[131, 133, 54354]))


def update_car_info(**car):
    car['is_available'] = True
    return car


print(update_car_info(brand='Mercedes', price=125_000))
