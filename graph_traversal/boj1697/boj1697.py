import sys;
from collections import deque;

def parseInput():
  n, k = map(int, sys.stdin.readline().split());
  return n, k;

def bfs(queue, dist, k):
  while queue:
    cur = queue.popleft();
    if (cur == k): return dist[cur];
    for new in [cur + 1, cur - 1, cur * 2]:
      if (new < 0 or new > 1000000): continue;
      if (dist[new] != -1): continue;
      queue.append(new);
      dist[new] = dist[cur] + 1;
  return -1;

def solution(args):
  n, k = args;
  queue = deque();
  dist = [-1] * 1000004;
  dist[n] = 0;
  queue.append(n);
  result = bfs(queue, dist, k);
  return result;

result = solution(parseInput());
print(result);
