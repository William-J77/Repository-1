vowels = ["a", "e", "i", "o", "u"]

# Write your function here

def vowel_counter(string):
  result = 0
  for v in string:
    if v in ["a", "e", "i", "o", "u"]:
      result += 1
  return result

print(vowel_counter("supercalifragilisticexpialidocious"))