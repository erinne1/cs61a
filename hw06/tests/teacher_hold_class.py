test = {
  'name': 'teacher_hold_class',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define student-rachel (student-create 'rachel '(astronomy)))
          student-rachel
          scm> (define student-lucy (student-create 'lucy '(astronomy astronomy)))
          student-lucy
          scm> (define students (cons student-rachel (cons student-lucy nil)))
          students
          scm> (define teacher-pamela (teacher-create 'pamela 'cs61a students))
          teacher-pamela
          scm> (define teacher-pamela (teacher-hold-class teacher-pamela)) ; pamela holds class!
          teacher-pamela
          scm> (map student-get-name (teacher-get-students teacher-pamela))
          (rachel lucy)
          scm> (map student-get-classes (teacher-get-students teacher-pamela))
          ((cs61a astronomy) (cs61a astronomy astronomy))
          scm> (define teacher-paul (teacher-create 'paul 'cs61b (teacher-get-students teacher-pamela))) ; paul works with pamela's students
          teacher-paul
          scm> (define teacher-paul (teacher-hold-class teacher-paul)) ; paul holds class!
          teacher-paul
          scm> (map student-get-classes (teacher-get-students teacher-paul))
          ((cs61b cs61a astronomy) (cs61b cs61a astronomy astronomy))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load "./hw06.scm")
      scm> (load "./tests/alternate_teachers_students.scm")  ; abstraction check: load different abstraction!
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
