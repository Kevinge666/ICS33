def nested_count(l: 'any nested list of int', a: int) -> int:
    if l == []:
        return 0
    if type(l[0]) == int:
        if l[0] == a:
            return 1 + nested_count(l[1:], a)
        else:
            return 0 + nested_count(l[1:], a)
    elif type(l[0]) is list:
        return nested_count(l[0], a) + nested_count(l[1:], a)
    else:
        return 0 + nested_count(l[1:], a)


if __name__ == '__main__':
    print('\nTesting nested_count')
    print(nested_count([1, 2, 4, 1, 8, 1, 3, 2, 1, 1], 1))
    print(nested_count([[1, 2, 4, 1, 8], [1, 3, 2], 1, 1], 1))
    print(nested_count([[1, 2, [4, [1], 8], [1, 3, 2]], [1, 1]], 1))
