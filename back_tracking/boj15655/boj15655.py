import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  arr = list(map(int, sys.stdin.readline().split()));
  arr.sort();
  return n, m, arr;

def backtracking(*args):
  depth, cur, m, arr, result, sequence, used = args;
  if (depth == m):
    result.append(sequence[:]);
    return;
  for idx, nxt in enumerate(arr):
    if (used[idx]): continue;
    if (cur >= nxt): continue;
    sequence.append(nxt);
    used[idx] = True;
    backtracking(depth + 1, nxt, m, arr, result, sequence, used);
    sequence.pop();
    used[idx] = False;


def solution(args):
  n, m, arr = args;
  result, sequence = [], [];
  used = [False] * (n + 1);
  backtracking(0, 0, m, arr, result, sequence, used);
  return result;

result = solution(parseInput());
[print(*sequence) for sequence in result];
