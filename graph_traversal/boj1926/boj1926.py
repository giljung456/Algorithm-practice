import sys;
from collections import deque;

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)];
  return n, m, board;

def getArea(visited, board, startXY, n, m):
  queue = deque();
  dx = (1, 0, -1, 0);
  dy = (0, 1, 0, -1);
  queue.append(startXY);
  x, y = startXY
  visited[x][y] = True;
  area = 0;
  while queue:
    curX, curY = queue.popleft();
    area += 1;
    for biasX, biasY in zip(dx, dy):
      newX, newY = curX + biasX, curY + biasY;
      if (newX < 0 or newX >= n): continue;
      if (newY < 0 or newY >= m): continue;
      if (visited[newX][newY] or not board[newX][newY]): continue;
      queue.append((newX, newY));
      visited[newX][newY] = True;
  return area;

def solution(args):
  n, m, board = args;
  visited = [[False] * m for _ in range(n)];
  maxArea = cnt = 0;
  for i in range(n):
    for j in range(m):
        if (visited[i][j] or not board[i][j]): continue;
        cnt += 1;
        area = getArea(visited, board, (i, j), n, m);
        maxArea = max(maxArea, area);
  return cnt, maxArea;

cnt, maxArea = solution(parseInput());
print(cnt);
print(maxArea);
