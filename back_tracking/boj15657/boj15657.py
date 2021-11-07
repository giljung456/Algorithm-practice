import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  arr = list(map(int, sys.stdin.readline().split()));
  arr.sort();
  return n, m, arr;

def backtracking(*args):
  depth, cur, m, arr, result, sequence = args;
  if (depth == m):
    result.append(sequence[:]);
    return;
  for nxt in arr:
    if (cur > nxt): continue;
    sequence.append(nxt);
    backtracking(depth + 1, nxt, m, arr, result, sequence);
    sequence.pop();


def solution(args):
  n, m, arr = args;
  result, sequence = [], [];
  backtracking(0, 0, m, arr, result, sequence);
  return result;

result = solution(parseInput());
[print(*sequence) for sequence in result];
