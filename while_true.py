while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

if x > 0:
    print('Hi')
elif x < 0:
    print('Hallo')
else:
    print('Bye')

