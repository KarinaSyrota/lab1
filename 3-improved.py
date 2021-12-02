first_num = 2
second_num = 3


def add(x, y):
    return x + y


def sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


result = add(first_num, second_num)

print({'sum': result})
print(sum(5, 6, 9))
