"""
algorithme de recherche : recherche linéaire

"""

numbers = [1,78,45,200,7,3,0,56]

search_for = 0

result = -1

for i in range(len(numbers) - 1):
    if search_for == numbers[i]:
        result = i
        break

print(result)