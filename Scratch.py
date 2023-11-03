def sort_pair(input_tuple):
    (a, b) = input_tuple
    if a < b:
        return a, b
    else:
        return b, a


print(sort_pair((3, 5)))
