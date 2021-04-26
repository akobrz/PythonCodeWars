def remove_smallest(numbers):
    return [x for i, x in enumerate(numbers) if i != numbers.index(min(numbers))]

print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([]))
