import random
import string

print(random.random())
print(random.randint(23, 54))
print(random.choice([2, 3, 4, 5, 6]))
print(random.choices([2, 3, 4, 5, 6], k=3))
print("".join(random.choices("dgrekndlmsdcfr", k=4)))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

print(string.ascii_letters)
print(string.digits)

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)