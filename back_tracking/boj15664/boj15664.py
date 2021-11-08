import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  arr = list(map(int, sys.stdin.readline().split()));
  return n, m, sorted(arr);

def backtracking(*args):
  depth, cur, n, m, arr, result, sequence, used = args;
  if (depth == m):
    result.append(sequence[:]);
    return;
  pre = 0;
  for idx, nxt in enumerate(arr):
    if (used[idx]): continue;
    if (nxt == pre): continue;
    if (cur > nxt): continue;
    used[idx] = True;
    pre = nxt;
    sequence.append(nxt);
    backtracking(depth + 1, nxt, n, m, arr, result, sequence, used);
    used[idx] = False;
    sequence.pop();

def solution(*args):
  n, m, arr = args;
  result, sequence = [], [];
  used = [False] * (n + 1);
  backtracking(0, 0, n, m, arr, result, sequence, used);
  return result;

result = solution(*parseInput());
[print(*sequence) for sequence in result];
