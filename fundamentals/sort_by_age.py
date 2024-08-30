def sort_by_age(lst):
    return sorted(lst, key=lambda x: x[1])

people=[("Xavi",25),("Sinopa",19),("Monclare",30)]

sorted_people = sort_by_age(people)

print(sorted_people)