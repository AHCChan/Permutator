"""
SIMPLE PERMUTATOR
(version 1.0)
by Angelo Chan

This is a library containing simple functions used to generate an exhaustive
list of all unique permutations for a unidimensional collection of values.

The functions are not optimized and therefore, only suitable for small
collections.

The function also does not work with multi-dimensional data.

Example:
    INPUT:
        [2, 1, 1, 0]
    OUTPUT:
        [
            [2, 1, 1, 0],
            [2, 1, 0, 1],
            [2, 0, 1, 1],
            [1, 2, 1, 0],
            [1, 2, 0, 1],
            [1, 1, 2, 0],
            [1, 1, 0, 2],
            [1, 0, 2, 1],
            [1, 0, 1, 2],
            [0, 2, 1, 1],
            [0, 1, 2, 1],
            [0, 1, 1, 2]
        ]    
"""



# Functions ####################################################################

def Simple_Permutate(collection):
    """
    Generate an exhaustive list of all permutations of the list or tuple given
    as input for this function.
    
    All permutations are returned as lists, even if the original input was a
    tuple.
    
    @collection
            (list/tuple<x>)
            The collection of values to be permutated.
    
    Simple_Permutate(list) -> list<list<x>>
    Simple_Permutate(tuple) -> list<list<x>>
    """
    # (recursion loop handler)
    if len(collection) == 1:
        return [collection]
    
    # Extract raw
    all_values = sorted(collection)
    length = len(all_values)
    range_ = range(length)
    
    # Setup
    unique = set([])
    result = []
    
    # Loop (main recursion body)
    for i in range_:
        copy = list(all_values)
        value = copy.pop(i)
        sub_permutations = Simple_Permutate(copy)
        for j in range_:
            for sub in sub_permutations:
                temp = list(sub)
                temp.insert(j, value)
                tup = tuple(temp)
                if tup not in unique:
                    unique.add(tup)
                    result.append(temp)
    
    # Return
    return result


