"""
algorithme de tri  : tri bulle

"""

numbers = [8,3,5,0,9,2,4,7,1,6]

#indicateur qui marque la fin de la boucle
flag = True

while flag:
    flag = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            flag = True

print(numbers)