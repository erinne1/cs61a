test = {
  'name': 'student_attend_class',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define student-rachel (student-create 'rachel '(astronomy))) ; a student named rachel who has attended astronomy once
          student-rachel
          scm> (define student-rachel (student-attend-class student-rachel 'chemistry))
          student-rachel
          scm> (student-get-classes student-rachel)
          (chemistry astronomy)
          scm> (define student-rachel (student-attend-class student-rachel 'history))
          student-rachel
          scm> (student-get-classes student-rachel)
          (history chemistry astronomy)
          scm> (student-get-name student-rachel)
          rachel
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load "./tests/alternate_teachers_students.scm")  ; abstraction check: load different abstraction!
      scm> (load "./hw06.scm")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
