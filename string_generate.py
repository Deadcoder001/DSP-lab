import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_until_match(target_string):
    length = len(target_string)
    generated_string = ''

    while True:
        generated_string = generate_random_string(length)
        print(generated_string)

        if generated_string == target_string:
            break

    return generated_string


target_string = "Hello123"
result = generate_until_match(target_string)

print(f"Target string '{target_string}' generated successfully.")
