import sys;
from functools import reduce

calc = {
  0 : lambda x, y : x + y,
  1 : lambda x, y : x - y,
  2 : lambda x, y : x * y,
  3 : lambda x, y : (abs(x) // y) * (x // abs(x)) if x != 0 else 0
} 

def parseInput():
  n = int(sys.stdin.readline());
  arr = list(map(int, sys.stdin.readline().split()));
  operatorCnt = list(map(int, sys.stdin.readline().split()));
  operators = reduce(lambda acc, cur: acc + [cur] * operatorCnt[cur], range(4), []);
  return n, arr, operators;

def resultFuncs():
  maxValue = -float('inf');
  minValue = float('inf');
  def getResult(): return maxValue, minValue;
  def updateResult(newValue):
    nonlocal maxValue, minValue;
    maxValue = max(maxValue, newValue);
    minValue = min(minValue, newValue);
  return getResult, updateResult;

def backtracking(*args):
  depth, n, arr, operators, isUsed, sequence, updateResult = args;
  if (depth == n - 1):
    newValue = reduce(lambda acc, idx: calc[sequence[idx]](acc, arr[idx + 1]), range(n - 1), arr[0]);
    updateResult(newValue);
    return;
  pre = -1;
  for idx, nxt in enumerate(operators):
    if (isUsed[idx]): continue;
    if (pre == nxt): continue;
    pre = nxt;
    isUsed[idx] = True;
    sequence.append(nxt);
    backtracking(depth+1, n, arr, operators, isUsed, sequence, updateResult);
    isUsed[idx] = False;
    sequence.pop();

def solution(*args):
  n, arr, operators = args;
  isUsed, sequence = [False] * (n - 1), [];
  getResult, updateResult = resultFuncs();
  backtracking(0, n, arr, operators, isUsed, sequence, updateResult);
  return getResult();


maxValue, minValue = solution(*parseInput());
[print(result) for result in [maxValue, minValue]];
