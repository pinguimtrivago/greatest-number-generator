import random

try:
    min_num = int(input("First number: "))
    max_num = int(input("Second number: "))

    if min_num > max_num:
        print("Learn math.")
    else:
        random_num = random.randint(min_num, max_num)
        print(f"{random_num}. Cool number, i guess.")

except ValueError:
    print("Numbers, dumbass.")
