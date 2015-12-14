test = {
  'name': 'Height',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab05 import *
          >>> def height(t):
          ...     if is_leaf(t):
          ...         return 0
          ...     return 1 + max([height(b) for b in branches(t)])
          >>> t = tree(1, [tree(2, [tree(3)])])
          >>> height(t)
          2
          >>> t = tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])
          >>> height(t)
          2
          >>> t = tree(1, [tree(2), tree(3, [tree(5)])])
          >>> height(t)
          2
          >>> t = tree(1)
          >>> height(t)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from lab05 import *
          >>> def height(t):
          ...     if is_leaf(t):
          ...         current_height = 0
          ...     else:
          ...         current_height = 1 + max([height(subtree) for subtree in subtrees(t)])
          ...     print(current_height)
          ...     return current_height
          >>> t = tree(1, [tree(2, [tree(3)])])
          >>> height(t)
          58e1f1fb97222d3a4c3904f2aa3cf3fa
          35926b8dc788659825b34f78c7f76f91
          31f02e75f8bef5a0621b68131795447b
          31f02e75f8bef5a0621b68131795447b
          # locked
          >>> t = tree(1, [tree(2), tree(3, [tree(5)]), tree(4)])
          >>> height(t)
          58e1f1fb97222d3a4c3904f2aa3cf3fa
          58e1f1fb97222d3a4c3904f2aa3cf3fa
          35926b8dc788659825b34f78c7f76f91
          58e1f1fb97222d3a4c3904f2aa3cf3fa
          31f02e75f8bef5a0621b68131795447b
          31f02e75f8bef5a0621b68131795447b
          # locked
          >>> t = tree(1, [tree(2), tree(3, [tree(5)])])
          >>> height(t)
          58e1f1fb97222d3a4c3904f2aa3cf3fa
          58e1f1fb97222d3a4c3904f2aa3cf3fa
          35926b8dc788659825b34f78c7f76f91
          31f02e75f8bef5a0621b68131795447b
          31f02e75f8bef5a0621b68131795447b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}