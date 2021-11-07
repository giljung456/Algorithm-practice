import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  return n, m;

def backtracking(*args):
  depth, cur, n, m, result, used, sequence = args;
  if (depth == m):
    result.append(sequence[:]);
    return;
  for nxt in range(1, n + 1):
    if (used[nxt]): continue;
    if (cur >= nxt): continue;
    used[nxt] = True;
    sequence.append(nxt);
    backtracking(depth + 1, nxt, n, m, result, used, sequence);
    used[nxt] = False;
    sequence.pop();

def solution(args):
  n, m = args;
  result = [];
  sequence = [];
  used = [False] * (n + 1);
  backtracking(0, 0, n, m, result, used, sequence);
  return result;

result = solution(parseInput());
[print(*sequence) for sequence in result];
