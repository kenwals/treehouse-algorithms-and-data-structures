import random
"""this is a bad method of sorting, Avoid!!

    Returns:
        [type]: [description]
"""


numbers = [50,8,100,4,7,52,11,45]

def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index +1]:
            return False
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts +=1
    return values

print(bogo_sort(numbers))
