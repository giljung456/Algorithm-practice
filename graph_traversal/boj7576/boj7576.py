import sys;
from collections import deque;

def parseInput():
  m, n = map(int, sys.stdin.readline().split());
  store = [list(map(int, sys.stdin.readline().split())) for _ in range(n)];
  return n, m, store;

def canMove(*args):
  dist, n, m, store, newX, newY = args;
  if (newX < 0 or newX >= n): return False;
  if (newY < 0 or newY >= m): return False;
  if (dist[newX][newY] != -1): return False;
  if (store[newX][newY] == -1): return False;
  return True;

def bfs(*args):
  queue, dist, n, m, store = args;
  dx, dy = (1, 0, -1, 0), (0, 1, 0, -1);
  while queue:
    curX, curY = queue.popleft();
    for biasX, biasY in zip(dx, dy):
      newX, newY = curX + biasX, curY + biasY;
      if (not canMove(dist, n, m, store, newX, newY)): continue;
      queue.append((newX, newY));
      dist[newX][newY] = dist[curX][curY] + 1;

def solution(args):
  n, m, store = args;
  queue = deque();
  result = 0;
  dist = [[-1] * m for _ in range(n)];
  for i in range(n):
    for j in range(m):
      if (store[i][j] != 1): continue;
      dist[i][j] = 0;
      queue.append((i, j));
  bfs(queue, dist, n, m, store);
  for i in range(n):
    for j in range(m):
      if (dist[i][j] == -1 and store[i][j] == 0): return -1;
      result = max(result, dist[i][j]);
  return result;

result = solution(parseInput());
print(result);
