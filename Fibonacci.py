def fib(index):
    first_fib = 0
    second_fib = 1
    i = 0
    while i < index - 2:
        fib_next = first_fib + second_fib
        first_fib = second_fib
        second_fib = fib_next
        i += 1
    print(second_fib)


fib(6)




