def find_mirror_characters(input_str):
    mirror_dict = {'A': 'A', 'B': 'C', 'C': 'B', 'D': 'D', 'E': '3', '3': 'E'}

    mirrored_str = ''
    for char in reversed(input_str):
        mirrored_str += mirror_dict.get(char, char)

    return mirrored_str


input_string = "ABCED3"
mirrored_result = find_mirror_characters(input_string)

print("Original String:", input_string)
print("Mirrored String:", mirrored_result)
