def is_happy_ticket(ticket_number: str):
    i = 0
    x = len(ticket_number) // 2
    first_half_numbers = ''
    second_half_numbers = ''
    while i <= (len(ticket_number) - 1) // 2:
        first_half_numbers = first_half_numbers + ticket_number[i]
        i += 1

    while x < len(ticket_number):
        second_half_numbers = second_half_numbers + ticket_number[x]
        x += 1

    first_list = list(first_half_numbers)
    second_list = list(second_half_numbers)
    first_int_list = [eval(index) for index in first_list]
    second_int_list = [eval(index1) for index1 in second_list]

    if sum(first_int_list) == sum(second_int_list):
        return True
    else:
        return False


print(is_happy_ticket('123514212122415321'))
