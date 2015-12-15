def map_and_filter(s, map_fn, filter_fn):
    """Return a new list containing the result of calling map_fn on each
    element of sequence s for which filter_fn returns a true value.

    >>> square = lambda x: x * x
    >>> is_odd = lambda x: x % 2 == 1
    >>> map_and_filter([1, 2, 3, 4, 5], square, is_odd)
    [1, 9, 25]
    """
    # BEGIN Question 0
    "*** REPLACE THIS LINE ***"
    return [map_fn(x) for x in s if filter_fn(x)]

def key_of_min_value(d):
    """Returns the key in dict d that corresponds to the minimum value of d.

    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """
    # BEGIN Question 0
    "*** REPLACE THIS LINE ***"
    return min(x for x, y in d.items() if y == min(d.values()))
    # END Question 0


def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and the
    i-th element of s.

    >>> enumerate([6, 1, 'a'])
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """
    # BEGIN Question 0
    "*** REPLACE THIS LINE ***"
    return zip(range(start, len(s)+start), s)