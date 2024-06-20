def is_nested(d):
  values = d.values()
  value_types = [type(elem) for elem in values]
  if type(()) in value_types or type([]) in value_types or type({}) in value_types:
    return True
  else:
    return False

# test code below
if __name__ == "__main__":
    example_dict = {
        1 : 'one',
        2 : 'two',
        3 : 'three'
    }

    print(is_nested(example_dict))  # Expected output: False

    example_dict = {
        1 : (2, 3),
        4 : 'four',
        5 : 'five'
    }

    print(is_nested(example_dict))  # Expected output: True

    example_dict = {
        1 : 'one',
        2 : {3 : 4},
        5 : 'five'
    }

    print(is_nested(example_dict))  # Expected output: True

    example_dict = {
        1 : 'one',
        2 : 'two',
        3 : [4, 5]
    }

    print(is_nested(example_dict))  # Expected output: True
