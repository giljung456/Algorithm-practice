from collections import deque
import sys

def parseInput():
  n, m = map(int, sys.stdin.readline().split());
  maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)];
  return n, m, maze;

def bfs(queue, maze, dist, n, m):
  dx = (1, 0, -1, 0);
  dy = (0, 1, 0, -1);
  queue.append((0, 0));
  dist[0][0] = 1;
  while queue:
    curX, curY = queue.popleft();
    for biasX, biasY in zip(dx, dy):
      newX, newY = curX + biasX, curY + biasY;
      if (newX < 0 or newX >= n): continue;
      if (newY < 0 or newY >= m): continue;
      if (not maze[newX][newY]): continue;
      if (dist[newX][newY] != -1): continue;
      queue.append((newX, newY));
      dist[newX][newY] = dist[curX][curY] + 1;

def solution(args):
  n, m, maze = args;
  dist = [[-1] * m for _ in range(n)];
  queue = deque();
  bfs(queue, maze, dist, n, m);
  return dist[n-1][m-1];

print(solution(parseInput()));
