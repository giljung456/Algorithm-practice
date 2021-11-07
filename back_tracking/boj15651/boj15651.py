import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  return n, m;

def backtracking(*args):
  depth, n, m, result, sequence = args;
  if (depth == m):
    result.append(sequence[:]);
    return;
  for nxt in range(1, n + 1):
    sequence.append(nxt);
    backtracking(depth + 1, n, m, result, sequence);
    sequence.pop();

def solution(args):
  n, m = args;
  result, sequence = [], [];
  backtracking(0, n, m, result, sequence);
  return result;

result = solution(parseInput());
[print(*sequence) for sequence in result];