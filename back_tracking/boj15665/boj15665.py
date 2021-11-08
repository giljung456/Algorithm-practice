import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  arr = list(map(int, sys.stdin.readline().split()));
  return n, m, sorted(arr);

def backtracking(*args):
  depth, n, m, arr, result, sequence = args;
  if (depth == m):
    result.append(sequence[:]);
    return;
  pre = 0;
  for nxt in enumerate(arr):
    if (nxt == pre): continue;
    pre = nxt;
    sequence.append(nxt);
    backtracking(depth + 1, n, m, arr, result, sequence);
    sequence.pop();

def solution(*args):
  n, m, arr = args;
  result, sequence = [], [];
  backtracking(0, n, m, arr, result, sequence);
  return result;

result = solution(*parseInput());
[print(*sequence) for sequence in result];
