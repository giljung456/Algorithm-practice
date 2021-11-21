import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  return n, m;

def resultFuncs():
  result = 0;
  def getResult(): return result;
  def increaseResult():
    nonlocal result;
    result += 1;
  return getResult, increaseResult;

def backtracking(*args):
  depth, n, m, board, increaseResult = args;
  if (depth == n * m):
    increaseResult();
    return;
  backtracking(depth + 1, n, m, board, increaseResult);
  x, y = depth // m + 1, depth % m + 1;
  if (board[x-1][y] and board[x][y-1] and board[x-1][y-1]): return;
  board[x][y] = True;
  backtracking(depth + 1, n, m, board, increaseResult);
  board[x][y] = False;

def solution(*args):
  n, m = args;
  board = [[False] * (m + 1) for _ in range(n + 1)];
  getResult, increaseResult = resultFuncs();
  backtracking(0, n, m, board, increaseResult);
  return getResult();

result = solution(*parseInput());
print(result);
