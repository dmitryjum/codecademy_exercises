def prefix_function(pattern):
  pi = [0 for i in range(len(pattern))]
  for i in range(1, len(pattern)):
    if (pattern[:pi[i - 1] + 1] == pattern[i - pi[i - 1]:i + 1]):
      pi[i] = pi[i - 1] + 1
    elif (pattern[:pi[i - 1]] == pattern[i - pi[i - 1] + 1:i + 1]):
      pi[i] = pi[i - 1]
    else:
      for j in range(pi[i - 1], -1, -1):
        if (pattern[:j] == pattern[i - j + 1: i + 1]):
          pi[i] = j
          break