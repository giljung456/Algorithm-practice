import sys;
from collections import deque;

def parseInput():
  m, n, h = map(int, sys.stdin.readline().split());
  rows = [list(map(int, sys.stdin.readline().split())) for _ in range(n * h)];
  store = [rows[i:i+n] for i in range(0, n * h, n)];
  return h, n, m, store;

def canMove(*args):
  h, n, m, dist, store, newZ, newX, newY = args;
  if (newZ < 0 or newZ >= h): return False;
  if (newX < 0 or newX >= n): return False;
  if (newY < 0 or newY >= m): return False;
  if (dist[newZ][newX][newY] != -1): return False;
  if (store[newZ][newX][newY] == -1): return False;
  return True;

def bfs(*args):
  queue, dist, h, n, m, store = args;
  dx, dy, dz = (0, 1, 0, -1, 0, 0), (1, 0, -1, 0, 0, 0), (0, 0, 0, 0,1, -1);
  while queue:
    curZ, curX, curY = queue.popleft();
    for biasZ, biasX, biasY in zip(dz, dx, dy):
      newZ, newX, newY = curZ + biasZ, curX + biasX, curY + biasY;
      if (not canMove(h, n, m, dist, store, newZ, newX, newY)): continue;
      queue.append((newZ, newX, newY));
      dist[newZ][newX][newY] = dist[curZ][curX][curY] + 1;

def solution(args):
  h, n, m, store = args;
  result = 0;
  dist = [[[-1] * m for _ in range(n)] for _ in range(h)];
  queue = deque();
  for z in range(h):
    for x in range(n):
      for y in range(m):
        if (store[z][x][y] != 1): continue;
        dist[z][x][y] = 0;
        queue.append((z, x, y));
  bfs(queue, dist, h, n, m, store);
  for p in range(h):
    for q in range(n):
      for r in range(m):
        if (dist[p][q][r] == -1 and store[p][q][r] == 0): return -1;
        result = max(result, dist[p][q][r]);
  return result;

result = solution(parseInput());
print(result);
