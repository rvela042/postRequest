def swap(d):
    try:
        swapped_dict = {v: k for k, v in d.items()}
        return swapped_dict
    except TypeError:
        return "Cannot swap the keys and values for this dictionary"

# test code below
if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    swapped = swap(example_dict)
    print(swapped)
    # Your script should print: {'one': 1, 'two': 2, 'three': 3}

    example_dict = {
        1: [2, 3],
        4: 'four',
        5: 'five'
    }

    swapped = swap(example_dict)
    print(swapped)
    # Your script should print: Cannot swap the keys and values for this dictionary

    example_dict = {
        1: 'one',
        2: {3: 4},
        5: 'five'
    }

    swapped = swap(example_dict)
    print(swapped)
    # Your script should print: Cannot swap the keys and values for this dictionary

    example_dict = {
        1: 'one',
        2: 'two',
        3: (4, 5)
    }

    swapped = swap(example_dict)
    print(swapped)
    # Your script should print: {'one': 1, 'two': 2, (4, 5): 3}
