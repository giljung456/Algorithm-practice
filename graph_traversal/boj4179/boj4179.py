import sys;
from collections import deque;

def parseInput():
  x, y = map(int, sys.stdin.readline().split());
  maze = [list(sys.stdin.readline().strip()) for _ in range(x)];
  return x, y, maze;

def canMove(*args):
  x, y, maze, newX, newY, time = args;
  if (newX < 0 or newX >= x): return False;
  if (newY < 0 or newY >= y): return False;
  if (maze[newX][newY] == '#'): return False;
  if (time[newX][newY] != -1): return False;
  return True;

def fireBfs(*args):
  queue, time, x, y, maze = args;
  dx, dy = (1, 0, -1, 0), (0, 1, 0, -1);
  while queue:
    curX, curY = queue.popleft();
    for biasX, biasY in zip(dx, dy):
      newX, newY = curX + biasX, curY + biasY;
      if (not canMove(x, y, maze, newX, newY, time)): continue;
      queue.append((newX, newY));
      time[newX][newY] = time[curX][curY] + 1;

def jihunBfs(*args):
  queue, jihunTime, fireTime, x, y, maze = args;
  dx, dy = (1, 0, -1, 0), (0, 1, 0, -1);
  while queue:
    curX, curY = queue.popleft();
    if (curX == 0 or curX == x - 1): return True, jihunTime[curX][curY] + 1;
    if (curY == 0 or curY == y - 1): return True, jihunTime[curX][curY] + 1;
    for biasX, biasY in zip(dx, dy):
      newX, newY = curX + biasX, curY + biasY;
      if (not canMove(x, y, maze, newX, newY, jihunTime)): continue;
      if (jihunTime[curX][curY] + 1 >= fireTime[newX][newY] and fireTime[newX][newY] != -1): continue;
      queue.append((newX, newY));
      jihunTime[newX][newY] = jihunTime[curX][curY] + 1;
  return False, -1;

def solution(args):
  x, y, maze = args;
  jihunQueue, fireQueue = deque(), deque();
  jihunTime, fireTime = [[-1] * y for _ in range(x)], [[-1] * y for _ in range(x)];
  for i in range(x):
    for j in range(y):
      if (maze[i][j] == 'J'):
        jihunQueue.append((i, j));
        jihunTime[i][j] = 0;
      if (maze[i][j] == 'F'):
        fireQueue.append((i, j));
        fireTime[i][j] = 0;
  fireBfs(fireQueue, fireTime, x, y, maze);
  canEscape, result = jihunBfs(jihunQueue, jihunTime,fireTime, x, y, maze);
  return result if canEscape else 'IMPOSSIBLE';

result = solution(parseInput());
print(result);
