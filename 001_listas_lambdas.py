numbers_list = [
    8,
    10,
    23,
    38,
    126,
    128,
    18,
    19,
    22,
    9,
]


def double_number(value):
    return value * 2


print("------------------------------")
for n in numbers_list:
    r = double_number(n)
    print(f'Calculando el doble de {n}: {r}')

number = 2500
number_double = double_number(number)
print("------------------------------")
print(f'Calculando el doble de {number}: {double_number}')

print("#-----------------------------------------")
# apply double_number using map
numbers_list_double = list(map(double_number,numbers_list))
print(numbers_list)
print(numbers_list_double)

# apply double_number using lambda
print("#--------------------------------------------")
double = lambda value: value * 2
print(double(5000))