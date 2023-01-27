def prefix_function(pattern):
	pi = [0 for i in range(len(pattern))]
	for i in range(1, len(pattern)):
		j = pi[i - 1]
		while (j > 0 and pattern[i] != pattern[j]):
			j = pi[j - 1]
		if (pattern[i] == pattern[j]):
			j += 1
		pi[i] = j
	return pi


def kmp_algorithm(pattern, text):
  m = len(pattern)
  n = len(text)
  pi = prefix_function(pattern)
  j = 0
  count = 0
  for i in range(n):
    while (j > 0 and text[i] != pattern[j]):
      j = pi[j - 1]
    if (text[i] == pattern[j]):
      j += 1
    if (j == m):
      count += 1
    pi[i] = j
  return count
