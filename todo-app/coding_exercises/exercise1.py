import random

def get_bounds():
    try:
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
    except ValueError:
        print('You did not input a valid whole number.')
        lower, upper = get_bounds()
    return lower, upper

def generate_random(lower, upper):
    return random.randint(lower, upper)

low, high = get_bounds()
random_number = generate_random(low, high)
print(random_number)