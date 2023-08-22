test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(1, Tree(2)) # Enter Function if you believe the answer is <function ...>, Error if it errors, and Nothing if nothing is displayed.
          feef61c63dd96e13f9fae6fd28442b2b
          # locked
          >>> t = Tree(1, [Tree(2)])
          >>> t.label
          7cd20da6435c318b417f99ab831ac85e
          # locked
          >>> t.branches[0]
          6e3e150dcaf43b1aee92209a3f22f19f
          # locked
          >>> t.branches[0].label
          32cd207d18df99546ca7a56bc36ed715
          # locked
          >>> t.label = t.branches[0].label
          >>> t
          f331eaca6e463d6c1142a1cd9f252566
          # locked
          >>> t.branches.append(Tree(4, [Tree(8)]))
          >>> len(t.branches)
          32cd207d18df99546ca7a56bc36ed715
          # locked
          >>> t.branches[0]
          6e3e150dcaf43b1aee92209a3f22f19f
          # locked
          >>> t.branches[1]
          7120759eec12bcbd774a96e9ae93b1e9
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
