import sys;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)];
  return n, m, arr;

def resultFuncs():
  result = 0;
  def getResult(): return result;
  def updateResult(candidate):
    nonlocal result;
    result = max(result, candidate);
  return getResult, updateResult;

def backtracking(*args):
  depth, intensity, isUsed, n, m, arr, updateResult = args;
  if (depth == n * m):
    updateResult(intensity);
    return;
  backtracking(depth + 1, intensity, isUsed, n, m, arr, updateResult);
  x, y = depth // m, depth % m;
  if (isUsed[x][y]): return;
  if (y-1 >= 0 and x+1 < n and not isUsed[x][y-1] and not isUsed[x+1][y]):
    isUsed[x][y] = isUsed[x][y-1] = isUsed[x+1][y] = True;
    addedIntensity = arr[x][y] * 2 + arr[x][y-1] + arr[x+1][y];
    backtracking(depth+1, intensity + addedIntensity, isUsed, n, m, arr, updateResult);
    isUsed[x][y] = isUsed[x][y-1] = isUsed[x+1][y] = False;
  if (y-1 >= 0 and x-1 >= 0 and not isUsed[x][y-1] and not isUsed[x-1][y]):
    isUsed[x][y] = isUsed[x][y-1] = isUsed[x-1][y] = True;
    addedIntensity = arr[x][y] * 2 + arr[x][y-1] + arr[x-1][y];
    backtracking(depth+1, intensity + addedIntensity, isUsed, n, m, arr, updateResult);
    isUsed[x][y] = isUsed[x][y-1] = isUsed[x-1][y] = False;
  if (x-1 >= 0 and y+1 < m and not isUsed[x-1][y] and not isUsed[x][y+1]):
    isUsed[x][y] = isUsed[x-1][y] = isUsed[x][y+1] = True;
    addedIntensity = arr[x][y] * 2 + arr[x-1][y] + arr[x][y+1];
    backtracking(depth+1, intensity + addedIntensity, isUsed, n, m, arr, updateResult);
    isUsed[x][y] = isUsed[x-1][y] = isUsed[x][y+1] = False;
  if (x+1 < n and y+1 < m and not isUsed[x+1][y] and not isUsed[x][y+1]):
    isUsed[x][y] = isUsed[x+1][y] = isUsed[x][y+1] = True;
    addedIntensity = arr[x][y] * 2 + arr[x+1][y] + arr[x][y+1];
    backtracking(depth+1, intensity + addedIntensity, isUsed, n, m, arr, updateResult);
    isUsed[x][y] = isUsed[x+1][y] = isUsed[x][y+1] = False;

def solution(*args):
  n, m, arr = args;
  getResult, updateResult = resultFuncs();
  isUsed = [[False] * m for _ in range(n)];
  backtracking(0, 0, isUsed, n, m, arr, updateResult);
  return getResult();

result = solution(*parseInput());
print(result);
