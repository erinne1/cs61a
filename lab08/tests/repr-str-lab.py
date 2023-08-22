test = {
  'name': 'Repr-esentation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A:
          ...   def __init__(self, x):
          ...         self.x = x
          ...   def __repr__(self):
          ...         return self.x
          ...   def __str__(self):
          ...         return self.x * 2
          >>> class B:
          ...   def __init__(self):
          ...         print('boo!')
          ...         self.a = []
          ...   def add_a(self, a):
          ...         self.a.append(a)
          ...   def __repr__(self):
          ...         print(len(self.a))
          ...         ret = ''
          ...         for a in self.a:
          ...               ret += str(a)
          ...         return ret
          >>> A('one')
          one
          >>> print(A('one'))
          oneone
          >>> repr(A('two'))
          'two'
          >>> b = B()
          boo!
          >>> b.add_a(A('a'))
          >>> b.add_a(A('b'))
          >>> b
          2
          aabb
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
