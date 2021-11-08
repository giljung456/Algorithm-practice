def parseInput():
  n = int(input());
  return n;

def resultFuncs():
  result = 0;
  def getResult(): return result;
  def increaseResult():
    nonlocal result;
    result += 1;
  return getResult, increaseResult;

def backtracking(*args):
  depth, n, used1, used2, used3, increaseResult = args;
  if (depth == n):
    increaseResult();
    return;
  for nxt in range(n):
    if (used1[nxt]): continue;
    if (used2[depth + nxt]): continue;
    if (used3[depth - nxt + n - 1]): continue;
    used1[nxt] = True;
    used2[depth + nxt] = True;
    used3[depth - nxt + n - 1] = True;
    backtracking(depth + 1, n, used1, used2, used3, increaseResult);
    used1[nxt] = False;
    used2[depth + nxt] = False;
    used3[depth - nxt + n - 1] = False;

def solution(n):
  used1 = [False] * n;
  used2 = [False] * (2*n-1);
  used3 = [False] * (2*n-1);
  getResult, increaseResult = resultFuncs();
  backtracking(0, n, used1, used2, used3, increaseResult);
  return getResult();

result = solution(parseInput());
print(result);
