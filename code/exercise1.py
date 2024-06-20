def find_key(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None

if __name__ == "__main__":
    example_dict = {
        1 : ['red', 'blue', 'green'],
        'Josh Jung' : (9, 10),
        3 : {0 : 0},
        9000 : 'impale mat a'
    }

    # Test Case 1
    key = find_key(example_dict, (9, 10))
    print(key)  # Should print 'Josh Jung'

    # Test Case 2
    key = find_key(example_dict, {0 : 0})
    print(key)  # Should print 3

    # Test Case 3
    key = find_key(example_dict, 'impale mat a')
    print(key)  # Should print 9000
