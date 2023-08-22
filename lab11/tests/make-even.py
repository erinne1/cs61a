test = {
  'name': 'make-even',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define t (tree 5 (list (tree 4 nil) (tree 7 nil))))
          t
          scm> (make-even t)
          (6 (4) (8))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 4 nil))
          t
          scm> (make-even t)
          (4)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 1 (list (tree 2 (list (tree 4 nil) (tree 5 nil))) (tree 3 (list (tree 6 nil) (tree 7 nil))))))
          t
          scm> (make-even t)
          (2 (2 (4) (6)) (4 (6) (8)))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define (tree label branches) (cons label branches))
      scm> (define (label t) (car t))
      scm> (define (branches t) (cdr t))
      scm> (define (is-leaf t) (null? (branches t)))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
