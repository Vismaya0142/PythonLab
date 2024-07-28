A = ['abc', 'xyz', 'aba', '1221']

def print_identical_first_last(lst):
    for index, item in enumerate(lst):
        if isinstance(item, str) and len(item) > 0 and item[0] == item[-1]:
            print(f"String: {item}, Index: {index}")

print_identical_first_last(A)
