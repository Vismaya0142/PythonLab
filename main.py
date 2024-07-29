# main.py

import dictionary_operations as do

def main():
    # Define multiple dictionaries for demonstration
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 2, 'c': 4, 'd': 5}
    dict3 = {'a': 1, 'b': 2, 'e': 6}

    print("Dictionaries:")
    print("dict1:", dict1)
    print("dict2:", dict2)
    print("dict3:", dict3)
    print()

    # Merge dictionaries
    merged = do.merging_dict(dict1, dict2, dict3)
    print("Merged Dictionary:")
    print(merged)
    print()

    # Find common keys
    common_keys = do.common_keys(dict1, dict2, dict3)
    print("Common Keys:")
    print(common_keys)
    print()

    # Invert a dictionary
    inverted = do.invert_dict(dict1)
    print("Inverted Dictionary (dict1):")
    print(inverted)
    print()

    # Find common key-value pairs
    common_pairs = do.common_key_value_pairs(dict1, dict2, dict3)
    print("Common Key-Value Pairs:")
    print(common_pairs)

if __name__ == "__main__":
    main()
