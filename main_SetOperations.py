# main_SetOperations.py

import module_SetOperations as mso

def main():
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}

    print("Initial sets:")
    print("s1:", s1)
    print("s2:", s2)
    print()

    print("Add element:")
    mso.add_element(s1, 4)
    print("s1:", s1)
    print()

    print("Remove element:")
    mso.remove_element(s1, 2)
    print("s1:", s1)
    print()

    print("Union and Intersection:")
    union, intersection = mso.union_and_intersection(s1, s2)
    print("Union:", union)
    print("Intersection:", intersection)
    print()

    print("Difference (s1 - s2):")
    print(mso.difference(s1, s2))
    print()

    print("Is Subset (s1 <= s2):")
    print(mso.is_subset(s1, s2))
    print()

    print("Set Length:")
    print(mso.set_length(s1))
    print()

    print("Symmetric Difference:")
    print(mso.symmetric_difference(s1, s2))
    print()

    print("Power Set:")
    print(mso.power_set(s1))
    print()

    print("Unique Subsets:")
    print(mso.unique_subsets(s1))

if __name__ == "__main__":
    main()
