from lab04 import *

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    if len(lst) == 0:
        return []
    if type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return [lst[0]] + flatten(lst[1:])

    


# Q13
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    # Iterative
    # new_lst = []
    # i, j = 0, 0
    # while i < len(lst1) and j < len(lst2):
    #     if lst1[i] <= lst2[j]:
    #         new_lst += [lst1[i]]
    #         i += 1
    #     else:
    #         new_lst += [lst2[j]]
    #         j += 1
    # while i < len(lst1):
    #     new_lst += [lst1[i]]
    #     i += 1
    # while j < len(lst2):
    #      new_lst += [lst2[j]]
    #      j += 1
    # return new_lst

    # Recursive 
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    if lst1[0] <= lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])        



