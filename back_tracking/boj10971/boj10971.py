import sys;

def parseInput():
  n = int(input());
  adj = [list(map(int, sys.stdin.readline().split())) for _ in range(n)];
  return n, adj;

def resultFuncs():
  result = float('inf');
  def getResult(): return result;
  def updateResult(newResult):
    nonlocal result;
    result = min(result, newResult);
  return getResult, updateResult;

def backtracking(*args):
  depth, cur, cost, n, adj, updateResult, used = args;
  if (depth == n-1):
    if (not adj[cur][0]): return;
    updateResult(cost + adj[cur][0]);
    return;
  for nxt, nxtCost in enumerate(adj[cur]):
    if (not nxtCost): continue;
    if (used[nxt]): continue;
    used[nxt] = True;
    backtracking(depth+1, nxt, cost+nxtCost, n, adj, updateResult, used);
    used[nxt] = False;

def solution(*args):
  n, adj = args;
  getResult, updateResult = resultFuncs();
  used = [False] * n;
  used[0] = True;
  backtracking(0, 0, 0, n, adj, updateResult, used);
  return getResult();

result = solution(*parseInput());
print(result);
