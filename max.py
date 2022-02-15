"""
l'algorithme nous permet de trouver le plus grand élément d'une liste d'entier

"""

nums = [10,2,8,78,7,6,0]

the_max = 0

for i in nums:
    if i > the_max:
        the_max = i

print(the_max)
