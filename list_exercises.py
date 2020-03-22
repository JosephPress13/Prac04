def get_numbers():
    numbers = []
    for i in range(5):
        number = int(input("Your numbers: "))
        numbers.append(number)
    print("First number is: {}".format(numbers[0]))
    print("Last number is: {}".format(numbers[-1]))
    print("The smallest number is: {}".format(min(numbers)))
    print("The largest number is: {}".format(max(numbers)))
    print("The average number is: {}".format((sum(numbers) / len(numbers))))


get_numbers()


def enter_username():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
                 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']
    username = input("Please enter your username:")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


enter_username()