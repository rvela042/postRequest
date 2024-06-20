def move_to_bottom(d, key):
    if key not in d:
        return "The key is not in the dictionary"
    
    value = d.pop(key)
    d[key] = value
    return d

# test code below
if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    result = move_to_bottom(example_dict, 1)
    print(example_dict if result == example_dict else result)
    # Your script should print: {2: 'two', 3: 'three', 1: 'one'}

    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    result = move_to_bottom(example_dict, 2)
    print(example_dict if result == example_dict else result)
    # Your script should print: {1: 'one', 3: 'three', 2: 'two'}

    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    result = move_to_bottom(example_dict, 4)
    print(result)
    # Your script should print: The key is not in the dictionary
