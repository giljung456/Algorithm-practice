import sys;

def resultFuncs():
  result = 0;
  def getResult(): return result;
  def increaseResult():
    nonlocal result;
    result += 1;
  return getResult, increaseResult;

def parseInput():
  n, s = map(int, sys.stdin.readline().split());
  arr = list(map(int, sys.stdin.readline().split()));
  return n, s, arr;

def backtracking(*args):
  depth, n, s, arr, getResult, increaseResult, sequence = args;
  if (depth == n):
    if (sum(sequence) == s and len(sequence)): increaseResult();
    return;
  sequence.append(arr[depth]);
  backtracking(depth + 1, n, s, arr, getResult, increaseResult, sequence);
  sequence.pop();
  backtracking(depth + 1, n, s, arr, getResult, increaseResult, sequence);


def solution(*args):
  n, s, arr = args;
  getResult, increaseResult = resultFuncs();
  sequence = [];
  backtracking(0, n, s, arr, getResult, increaseResult, sequence);
  return getResult();

result = solution(*parseInput());
print(result);
