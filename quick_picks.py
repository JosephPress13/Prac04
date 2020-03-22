import random

numbers_per_line = 6
minimum = 1
maximum = 45

def main():
    quick_picks = int(input("How many quick picks would you like to do? "))

    for i in range(quick_picks):
        quick_pick = []
        for j in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        # quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))

main()