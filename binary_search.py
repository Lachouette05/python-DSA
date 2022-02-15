"""
algo de recherche : recherche binaire

"""

numbers = [1,3,4,7,9,15,20,60]

search_for = 15

start = 0
end = len(numbers) - 1

found = False

while start <= end and not found:
    location = (start + end)//2
    if numbers[location] == search_for:
        found = True
    else:
        if search_for < numbers[location]:
            end = location - 1
        else:
            start = location + 1

print(found)
print(location)