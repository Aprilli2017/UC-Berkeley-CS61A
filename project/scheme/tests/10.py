test = {
  'name': 'Question 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> frame = global_frame.make_child_frame(Pair('a', Pair('b', Pair('c', nil))), Pair(1, Pair(2, Pair(3, nil))))
          >>> global_frame.lookup('a')
          afe8b0293088a787c654885143501f84
          # locked
          # choice: 1
          # choice: 2
          # choice: 3
          # choice: SchemeError
          >>> frame.lookup('a')
          7107157269a542fea41c45a208299f75
          # locked
          >>> frame.lookup('b')
          9ea224e62b219a1ee61849f282da5e65
          # locked
          >>> frame.lookup('c')
          5d8831cb01cb0c9d130940fa232fd534
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> frame = global_frame.make_child_frame(nil, nil)
          >>> frame.parent is global_frame
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> first = Frame(global_frame)
          >>> second = first.make_child_frame(nil, nil)
          >>> second.parent is first
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # More argument values than formal parameters
          >>> global_frame.make_child_frame(Pair('a', nil), Pair(1, Pair(2, Pair(3, nil))))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # More formal parameters than argument values
          >>> global_frame.make_child_frame(Pair('a', Pair('b', Pair('c', nil))), Pair(1, nil))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}