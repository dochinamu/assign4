fruit_dict = {}

while True:
    fruit = input('Enter a fruit type (q to quit): ')
    if fruit == 'q':
        break
    else:
        weight = input('Enter the weight in kg: ')
        fruit_dict[fruit] = weight
print()
print(fruit_dict)