class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[2]
    5
    >>> s
    Link(3, Link(4, Link(5)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)


class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def is_leaf(self):
        return not self.branches



def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    while s != Link.empty and s.rest != Link.empty:
        s.rest = s.rest.rest
        s = s.rest



def mutate_reverse(link):
    """Mutates the Link so that its elements are reversed.

    >>> link = Link(1)
    >>> mutate_reverse(link)
    >>> link
    Link(1)

    >>> link = Link(1, Link(2, Link(3)))
    >>> mutate_reverse(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    "*** YOUR CODE HERE ***"
    cur = link
    new_link = Link.empty
    while cur != Link.empty:
        new_link = Link(cur.first, new_link)
        cur = cur.rest
    link.first = new_link.first
    link.rest = new_link.rest



def long_paths(tree, n):
    """Return a list all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12)])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    Link(0, Link(1, Link(2)))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    Link(0, Link(6, Link(9)))
    Link(0, Link(11, Link(12)))
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    >>> long_paths(whole, 4)
    []
    """
    "*** YOUR CODE HERE ***"
    if tree.is_leaf():
        if n > 0:
            return []
        else:
            return [Link(tree.entry)]
    result = []
    for branch in tree.branches:
        for link in long_paths(branch, n-1):
            result += [Link(tree.entry, link)]
    # return [Link(tree.entry, link) for link in long_paths(branch, n-1) for branch in tree.branches]
    return result

def partial_tree(s, n):
    """Return a balanced tree of the first n elements of Link s, along with
    the rest of s.

    Examples of balanced trees:

    Tree(1)                      # leaf
    Tree(1, [Tree(2)])           # one branch is a leaf
    Tree(1, [Tree(2), Tree(3)])  # two branches with one node each

    Examples of unbalanced trees:

    Tree(1, [Tree(2, [Tree(3)])])            # one branch not a leaf
    Tree(1, [Tree(2),                        # Mismatch: branch with 1 node
             Tree(3, [Tree(4, [Tree(5)])])]) #        vs branch with 3 nodes

    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> partial_tree(s, 3)
    (Tree(2, [Tree(1), Tree(3)]), Link(4, Link(5)))
    >>> t = Link(-2, Link(-1, Link(0, s)))
    >>> partial_tree(t, 7)[0]
    Tree(1, [Tree(-1, [Tree(-2), Tree(0)]), Tree(3, [Tree(2), Tree(4)])])
    >>> partial_tree(t, 7)[1]
    Link(5)
    """
    if n == 1:
        return (Tree(s.first), s.rest)
    elif n == 2:
        return (Tree(s.first, [Tree(s.rest.first)]), s.rest.rest)
    else:
        left_size = (n-1)//2
        right_size = n - left_size - 1
        "*** YOUR CODE HERE ***"
        i = 0
        cur_list = s
        while i < left_size:
            cur_list = cur_list.rest
            i += 1
        remain_list = cur_list
        while i < n:
            remain_list = remain_list.rest
            i += 1
        return (Tree(cur_list.first, [partial_tree(s, left_size)[0], partial_tree(cur_list.rest, right_size)[0]]), remain_list)


def sequence_to_tree(s):
    """Return a balanced tree containing the elements of sorted Link s.

    Note: this implementation is complete, but the definition of partial_tree
    above is not complete.

    >>> sequence_to_tree(Link(1, Link(2, Link(3))))
    Tree(2, [Tree(1), Tree(3)])
    >>> elements = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7)))))))
    >>> sequence_to_tree(elements)
    Tree(4, [Tree(2, [Tree(1), Tree(3)]), Tree(6, [Tree(5), Tree(7)])])
    """
    return partial_tree(s, len(s))[0]

