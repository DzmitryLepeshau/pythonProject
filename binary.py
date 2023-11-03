def binary_sum(first_number: str, second_number: str):
    num_1 = int(first_number, 2)
    num_2 = int(second_number, 2)

    bin_summa = bin(num_1 + num_2)[2:]
    print(bin_summa)


binary_sum('101', '1010')

