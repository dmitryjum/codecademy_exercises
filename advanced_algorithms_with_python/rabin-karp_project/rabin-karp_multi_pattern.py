# def polynomial_hash(s):
#   hash_value = 0
#   for i in range(len(s)):
#     hash_value += (ord(s[i])*(26**(len(s) - i - 1)))
#   return hash_value
# def polynomial_rolling_hash(previous_hash, c1, c2, pattern_length):
#   return (previous_hash - ord(c1) * (26**(pattern_length - 1))) * 26 + ord(c2)
# def rabin_karp_algorithm_multiple(pattern, text):
#   pattern_dict = dict()
#   text_length = len(text)
#   for p in pattern:
#     pattern_hash = polynomial_hash(p)
#     pattern_dict[pattern_hash] = {
#       p: 0
#     }
#     pattern_length = len(p)
#     substring = text[: pattern_length]
#     substring_hash = polynomial_hash(substring)
#     if (pattern_hash == substring_hash):
#       pattern_dict[pattern_hash][p] += 1
#     for i in range(text_length - pattern_length):
#       previous_hash = substring_hash
#       substring_hash = polynomial_rolling_hash(previous_hash, text[i], text[i + pattern_length], pattern_length)
#       substring = text[i: i + pattern_length]
#       if (pattern_hash == substring_hash):
#         pattern_dict[pattern_hash][p] += 1
#   return pattern_dict
# patterns = ['ABC', 'BCD', 'CDE', 'DEF']
# text = 'ABCBCDCDEDEFCDE'
# # print(rabin_karp_algorithm_multiple(patterns, text))
# def rabin_karp_algorithm_2D(pattern, text):
#   two_d_dict = dict()
#   for t in text:
#     two_d_dict[t] = rabin_karp_algorithm_multiple(pattern, t)
#   return two_d_dict
# pattern = ['ABC', 'GHI']
# text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']
# print(rabin_karp_algorithm_2D(pattern, text))


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
  occurrences = 0
  m1 = len(pattern)
  m2 = len(pattern[0])
  n1 = len(text)
  n2 = len(text[0])
  #In each of the n1 rows of the text, there are n2 - m2 + 1 substrings of length m2
  #Meaning in "ABCDEF" 6 - 3 + 1 (4)substrings: ABC, BCD, CDE, DEF
  pattern_hash = 0
  for i in range(m1): #0..2
      pattern_hash += polynomial_hash(pattern[i])*(10**(m1 - i - 1))
  # print(pattern_hash)

  all_hashes = [[0 for j in range(n2 - m2 + 1)] for i in range(n1)]
  for i in range(n1):
    substring_hash = polynomial_hash(text[i][:m2])
    all_hashes[i][0] = substring_hash
    for j in range(n2 - m2): #(0,3)
      previous_hash = substring_hash #starts with the first hash for each i in n1
      substring_hash = polynomial_rolling_hash(previous_hash, text[i][j], text[i][j + m2], m2)
      all_hashes[i][j + 1] = substring_hash

  print(all_hashes)
  for j in range(n2 - m2 + 1):
    column_hash = 0
    for i in range(m1):
        column_hash += all_hashes[i][j]*(10**(m1 - i - 1))
    if (column_hash == pattern_hash):
        occurrences += 1
    for i in range(n1 - m1):
      previous_hash = column_hash
      column_hash = (previous_hash - all_hashes[i][j]*(10**(m1 - 1)))*10 + all_hashes[i + m1][j]
      if (column_hash == pattern_hash):
          occurrences += 1
  return occurrences

pattern = ['ABC', 'GHI']
text = ['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVWX', 'YZABCD', 'EFGHIJ', 'KLMNOP']
print(rabin_karp_algorithm_2D(pattern, text))











