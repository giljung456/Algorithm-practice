import sys;

def backtracking(*args):
  depth, word, isUsed, sequence, result = args;
  if (depth == len(word)):
    result.append(''.join(sequence));
    return;
  pre = 0;
  for idx, nxt in enumerate(word):
    if (isUsed[idx]): continue;
    if (nxt == pre): continue;
    isUsed[idx] = True;
    pre = nxt
    sequence.append(nxt);
    backtracking(depth+1, word, isUsed, sequence, result);
    isUsed[idx] = False;
    sequence.pop();

def solution(word):
  result, sequence = [], [];
  isUsed = [False] * len(word);
  backtracking(0, word, isUsed, sequence, result);
  return result;

t = int(input());
for i in range(t):
  word = sys.stdin.readline().strip();
  result = solution(sorted(word));
  [print(sequence) for sequence in result];
