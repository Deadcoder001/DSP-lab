def is_substring_present(main_string, substring):
    return substring in main_string

main_string = "Hello, World!"
substring_to_check = "World"

if is_substring_present(main_string, substring_to_check):
    print(f"'{substring_to_check}' is present in the given {main_string}.")
else:
    print(f"'{substring_to_check}' is not present in the given {main_string}.")
