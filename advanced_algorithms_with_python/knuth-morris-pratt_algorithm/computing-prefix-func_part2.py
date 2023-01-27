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
