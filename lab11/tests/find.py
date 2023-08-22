test = {
  'name': 'find',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define t (tree 1 (list (tree 2 (list (tree 4 nil) (tree 5 nil))) (tree 3 (list (tree 6 nil) (tree 7 nil))))))
          t
          scm> (find t 2)
          #t
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 1 (list (tree 2 (list (tree 4 nil) (tree 5 nil))) (tree 3 (list (tree 6 nil) (tree 7 nil))))))
          t
          scm> (find t 1)
          #t
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 1 (list (tree 2 (list (tree 4 nil) (tree 5 nil))) (tree 3 (list (tree 6 nil) (tree 7 nil))))))
          t
          scm> (find t 20)
          #f
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 3 nil))
          t
          scm> (find t 4)
          #f
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 3 nil))
          t
          scm> (find t 3)
          #t
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
