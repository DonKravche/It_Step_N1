# 1

squad_numbers = []

numbers = range(1, 11)

for number in numbers:
    number *= number
    squad_numbers.append(number)

print(squad_numbers)

# 2

chars_set = set()

user_string_input = str(input("Enter a text: "))

chars_to_remove = ';:=+-_.,/\\|\' '

correctedString = user_string_input.translate(str.maketrans('', '', chars_to_remove))

for char in correctedString:
    chars_set.add(char)

print(chars_set)

# 3

combined_tuple_set = set()
duplicated_values = []

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

for item in tuple1 + tuple2:
    if item in combined_tuple_set:
        if item not in duplicated_values:
            duplicated_values.append(item)
    else:
        combined_tuple_set.add(item)

print(combined_tuple_set)
print(duplicated_values)

# 4

tuplex = (1, 2, 3, 4)

swapped_tuple = (tuplex[-1], tuplex[1:-1], tuplex[0])

print(swapped_tuple)


# 5
def irl(irlTuple):
    result = []
    for items in irlTuple:
        if isinstance(items, tuple):
            result.extend(irl(items))
        else:
            result.append(items)
    return tuple(result)


irlTuple = (1, (2, 3), (4, (5, 6)))
print(f"output: {irl(irlTuple)}")


# 6

def bruh(x, y):
    new_set = set()
    for x_item in sorted(x):
        for y_item in sorted(y):
            new_set.add((x_item, y_item))
    return frozenset(new_set)


x = {1, 2}
y = {'a', 'b'}
result = bruh(x, y)
print(f"output: {set(result)}")
