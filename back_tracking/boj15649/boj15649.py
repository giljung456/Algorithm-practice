import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  return n, m;

def backtracking(*args):
  k, n, m, sequence, visited, result = args;
  if (k == m):
    result.append(sequence[:]);
    return;
  for nxt in range(1, n + 1):
    if (visited[nxt]): continue;
    sequence[k] = nxt;
    visited[nxt] = True;
    backtracking(k + 1, n, m, sequence, visited, result);
    visited[nxt] = False;

def solution(args):
  n, m = args;
  sequence = [-1] * m;
  visited = [False] * (n + 1);
  result = [];
  backtracking(0, n, m, sequence, visited, result);
  return result;

result = solution(parseInput());
[print(*sequence) for sequence in result];
