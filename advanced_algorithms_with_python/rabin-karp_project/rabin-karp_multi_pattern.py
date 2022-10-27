def polynomial_hash(s):
  hash_value = 0
  for i in range(len(s)):
    hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
  return hash_value
def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
  return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)
def rabin_karp_algorithm_multiple(pattern, text):
  pattern_dict = dict()
  text_length = len(text)
  for p in pattern:
    pattern_hash = polynomial_hash(p)
    pattern_dict[pattern_hash] = {
      p: 0
    }
    pattern_length = len(p)
    substring = text[: pattern_length]
    substring_hash = polynomial_hash(substring)
    if (pattern_hash == substring_hash):
      pattern_dict[pattern_hash][p] += 1
    for i in range(text_length - pattern_length):
      previous_hash = substring_hash
      substring_hash = polynomial_rolling_hash(previous_hash, text[i], text[i + pattern_length], pattern_length)
      substring = text[i: i + pattern_length]
      if (pattern_hash == substring_hash):
        pattern_dict[pattern_hash][p] += 1
  return pattern_dict
patterns = ['ABC', 'BCD', 'CDE', 'DEF']
text = 'ABCBCDCDEDEFCDE'
# print(rabin_karp_algorithm_multiple(patterns, text))
def rabin_karp_algorithm_2D(pattern, text):
  two_d_dict = dict()
  for t in text:
    two_d_dict[t] = rabin_karp_algorithm_multiple(pattern, t)
  return two_d_dict
pattern = ['ABC', 'GHI']
text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']
print(rabin_karp_algorithm_2D(pattern, text))



