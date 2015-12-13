test = {
  'name': 'Lambda Trivia',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 5
          >>> x = lambda x: lambda x: lambda y: 3+x
          >>> x(3)(5)(7)
          11f2dd23b3fd248f63abf27f5ba01f68
          # locked
          >>> you = 'fly'
          >>> yo, da = lambda do: you, lambda can: True
          >>> yo = yo('jedi')
          >>> da = (3 and 4 and 5 and (False or ' you shall'))
          >>> yo+da
          6791d141cfd767f288bc2f958f86dc31
          # locked
          >>> annoying = lambda yell: annoying
          >>> annoying('aiya')('aaa')('aaaa')('aaaaa')('aaaaaa')
          409d225c8d71bdae383b166e754adf05
          # locked
          >>> more = ' productive'
          >>> lip_service = lambda say: print(say)
          >>> useful_person = lambda do: do + more
          >>> lip_service('blah blah blah') + useful_person('be')
          70ad014c68a95974a94bff79cc9fa854
          9ee30c0bb2642a554fb2198e3b73feb1
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