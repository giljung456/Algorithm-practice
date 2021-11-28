import sys;

def resultFuncs():
  result = 0;
  def getResult(): return result;
  def updateResult(candidate):
    nonlocal result;
    result = max(result, candidate);
  return getResult, updateResult;

def backtracking(*args):
  depth, total, isUsed, potentials, updateResult = args;
  if (depth == 11):
    updateResult(total);
    return;
  for position in range(11):
    if(not potentials[depth][position]): continue;
    if (isUsed[position]): continue;
    isUsed[position] = True;
    backtracking(depth+1, total+potentials[depth][position], isUsed, potentials, updateResult);
    isUsed[position] = False;

def solution(potentials):
  getResult, updateResult = resultFuncs();
  isUsed = [False] * 11;
  backtracking(0, 0, isUsed, potentials, updateResult);
  return getResult();

t = int(input());
for _ in range(t):
  potentials = [list(map(int, sys.stdin.readline().split())) for _ in range(11)];
  result = solution(potentials);
  print(result);
