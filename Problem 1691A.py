def consecutiveSum(nTestCases = int(input())):
  for e in range(nTestCases):
    nSequence = [input() for e in range(2)]
    nElements = [int(e) for e in nSequence[0]]
    nSequenceList = [int(e) for e in nSequence[1].split(" ")]

    nEven = [e for e in nSequenceList if e % 2 == 0]
    nOdd  = [e for e in nSequenceList if e % 2 != 0]

    if len(nEven) < len(nOdd):
      print(len(nEven))
    else:
      print(len(nOdd))

consecutiveSum()
