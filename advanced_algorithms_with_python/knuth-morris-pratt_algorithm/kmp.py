def prefix_function(pattern):
  pi = [0 for i in range(len(pattern))]
  for i in range(1, len(pattern)):
    for j in range(1, i+1):
      if (pattern[:j] == pattern[i-j+1:i+1]):
        pi[i] = j