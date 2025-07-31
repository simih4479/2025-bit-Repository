# Ask user for width until
# they enter a number that is more tham zero
def int_check(question, low):

    error = f"Please enter a number that is more than zer{low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)



# main routine goes here
for item in range (0, 2):
    integer = int_check(question: "Integer: ", low: 0)
    print(Integer)

print()

for item in range (0, 2):
    height = int_check(question "Width: ", low: 1)
    print(width)

print()
for item in range (0, 2):
    height = int_check(question "Height: ", low: 1)
    print(height)
