# dictionary_operations.py

def merging_dict(*args):
    """Merges multiple dictionaries into one."""
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def common_keys(*args):
    """Finds common keys in multiple dictionaries."""
    if not args:
        return set()
    common = set(args[0].keys())
    for d in args[1:]:
        common.intersection_update(d.keys())
    return common

def invert_dict(d):
    """Inverts a dictionary, swapping keys and values."""
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            if isinstance(inverted_dict[value], list):
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key
    return inverted_dict

def common_key_value_pairs(*args):
    """Finds common key-value pairs across multiple dictionaries."""
    if not args:
        return set()
    common_pairs = set((k, v) for k, v in args[0].items())
    for d in args[1:]:
        common_pairs.intersection_update((k, v) for k, v in d.items())
    return common_pairs
