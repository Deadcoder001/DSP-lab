def can_become_empty(input_string):
    
    if not input_string:
        return True

    
    for i in range(1, len(input_string) + 1):
        new_string = input_string.replace(input_string[:i], '', 1)
        if new_string != input_string:
            
            if can_become_empty(new_string):
                return True

    return False


test_string = "abcabc"
result = can_become_empty(test_string)

if result:
    print(f'The string "{test_string}" can become empty by recursive deletion.')
else:
    print(f'The string "{test_string}" cannot become empty by recursive deletion.')

