import sys;

def parseInput():
  n = int(input());
  eggState = [list(map(int, sys.stdin.readline().split())) for _ in range(n)];
  return n, eggState;

def resultFuncs():
  result = -1;
  def getResult(): return result;
  def updateResult(newResult):
    nonlocal result;
    result = max(result, newResult);
  return getResult, updateResult;

def backtracking(*args):
  depth, n, eggState, updateResult, getResult = args;
  if (depth == n):
    breakCnt = len(list(filter(lambda state: state[0] <= 0, eggState)));
    updateResult(breakCnt);
    return;
  if (eggState[depth][0] <= 0):
    backtracking(depth+1, n, eggState, updateResult, getResult);
    return;
  finish = True;
  for nxt in range(n):
    s, _ = eggState[nxt];
    if (nxt == depth): continue;
    if (s <= 0): continue;
    finish = False;
    eggState[nxt][0] -= eggState[depth][1];
    eggState[depth][0] -= eggState[nxt][1];
    backtracking(depth+1, n, eggState, updateResult, getResult);
    eggState[nxt][0] += eggState[depth][1];
    eggState[depth][0] += eggState[nxt][1];
  if (finish): backtracking(n, n, eggState, updateResult, getResult);

def solution(*args):
  n, eggState = args;
  getResult, updateResult = resultFuncs();
  backtracking(0, n, eggState, updateResult, getResult);
  return getResult();

result = solution(*parseInput());
print(result);
