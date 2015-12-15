from lab07 import *

# Q5
def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return Tree(t.entry)
    new_branches = [cumulative_sum(branch) for branch in t.branches]
    total = 0
    for branch in new_branches:
        total += branch.entry
    return Tree(total+t.entry, new_branches)



# Q6
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"
    if len(lst) == 0:
        return Link.empty
    return Link(lst[0], list_to_link(lst[1:]))

# Q7
def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty:
        return []
    return [link.first] + link_to_list(link.rest)


# Q8
def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3)))
    >>> new = reverse(link)
    >>> print_link(new)
    <3 2 1>
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"
    def helper(front, back):
        if back == Link.empty:
            return front
        return helper(Link(back.first, front), back.rest)
    return helper(Link.empty, link)




# Q9
def deep_map(f, link):
    """Return a Link with the same structure as link but with fn mapped over
    its elements. If an element is an instance of a linked list, recursively
    apply f inside that linked list as well.

    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print_link(deep_map(lambda x: x * x, s))
    <1 <4 9> 16>
    >>> print_link(s) # unchanged
    <1 <2 3> 4>
    >>> print_link(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
    <<2 <4 6> 8> <<10>>>
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return Link.empty
    if isinstance(link.first, Link):
        return Link(deep_map(f, link.first), deep_map(f, link.rest))
    else:
        return Link(f(link.first), deep_map(f, link.rest))


# Q10
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    lst = []
    while not link is Link.empty:
        if link in lst:
            return True
        lst.append(link)
        link = link.rest
    return False


def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    def helper(link, original_link):
        if link is Link.empty:
            return False
        if link == original_link:
            return True
        return helper(link.rest, original_link)
    while not link is Link.empty:
        if helper(link.rest, link):
            return True
        link = link.rest
    return False

    # two pointer version
    # if link is Link.empty:
    #     return False
    # slow, fast = link, link.rest
    # while fast is not Link.empty:
    #     if fast.rest == Link.empty:
    #         return False
    #     elif fast == slow or fast.rest == slow:
    #         return True
    #     else:
    #         slow, fast = slow.rest, fast.rest.rest
    # return False 

