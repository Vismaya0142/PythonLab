# module_SetOperations.py

def add_element(s, element):
    """Adds an element to the set, ensuring no errors if the element is already present."""
    s.add(element)

def remove_element(s, element):
    """Removes an element from the set, ensuring no errors if the element is not present."""
    s.discard(element)

def union_and_intersection(s1, s2):
    """Returns the union and intersection of two sets, handling empty sets correctly."""
    return s1 | s2, s1 & s2

def difference(s1, s2):
    """Returns the difference S1 - S2, handling empty sets correctly."""
    return s1 - s2

def is_subset(s1, s2):
    """Checks if set S1 is a subset of set S2, handling empty sets correctly."""
    return s1 <= s2

def set_length(s):
    """Finds the length of a set without using the len() function."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    """Computes the symmetric difference of two sets."""
    return s1 ^ s2

def power_set(s):
    """Computes and displays the power set of a given set."""
    from itertools import chain, combinations
    
    s = list(s)
    power_set = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    
    
    for subset in power_set:
        print(set(subset))

def unique_subsets(s):
    """Gets all unique subsets of a given set."""
    return power_set(s)
