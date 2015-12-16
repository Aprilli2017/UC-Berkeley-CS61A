test = {
  'name': 'Question 9',
  'partner': 'A',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define (f x y) (+ x y))
          5e9740437eba0d6fc4d5ab5f9dd3d30b
          # locked
          scm> f
          2d318d142205ff0edf6e4b825290d4bc
          # locked
          # choice: (lambda (x y) (+ x y))
          # choice: (lambda (f x y) (+ x y))
          # choice: (f (x y) (+ x y))
          # choice: (define f (lambda (x y) (+ x y)))
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define (f) (+ 2 2))
          f
          scm> f
          (lambda () (+ 2 2))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (f x) (* x x))
          f
          scm> f
          (lambda (x) (* x x))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (define (foo x) 1 2 3 4 5)
          foo
          scm> foo
          (lambda (x) 1 2 3 4 5)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> inp = read_line("(define (f x) x)")
          >>> scheme_eval(inp, env)
          'f'
          >>> scheme_eval('f', env)
          LambdaProcedure(Pair('x', nil), Pair('x', nil), <Global Frame>)
          >>> inp == read_line("(define (f x) x)") # Don't mutate the input expression!
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      >>> from scheme import *
      >>> env = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}