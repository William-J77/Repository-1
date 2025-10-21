# Things to check:
# The `play_word` function does not add a word to an existing player's list, but instead overwrites the player's 
# words or adds a new player incorrectly. It should append the word to the player's list.

# def play_word(player, word):
#   if player in player_to_words:
#     player_to_words[player].append(word)
#   else:
#     player_to_words[player] = [word]
#   return player_to_words[player]

# The `update_point_totals` function works, but you should call it after using `play_word` to keep scores 
# in sync when a new word is played.

# play_word("player1", "DREAMS")
# update_point_totals("player1", "DREAMS")


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)} 
#Be sure not to use list actual names until the zip()

for letter, value in list(letter_to_points.items()):
    letter_to_points[letter.lower()] = value
#  for letter, value in list(letter_to_points.items()):
#     This loops through each key-value pair in the dictionary.
#     letter is the key (like “A”), value is the point value (like 1).
#     list() is used so you can safely add new keys to the dictionary while looping.

#     letter_to_points[letter.lower()] = value
#     This adds a new key to the dictionary: the lowercase version of letter,   with the same value.
#     For example, if letter is “A”, letter.lower() is “a”, so "a": 1 is added.


letter_to_points[" "] = 0 
#adds blank "tile" to scrabble

def score_word(word):
  point_total = 0
  for letter in word:
      point_total += letter_to_points.get(letter, 0)
      #dictionary.get(key_variable, default_value if key is not found)
  return point_total

print(letter_to_points)

brownie_points = score_word("BROWNIE")

print(brownie_points)

print()
print()

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Proof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

#Below, player, words defines the variable names, while player_to_words.items() will give each key:value pair one at a time through the loop. 
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = (player_points)

print(player_to_points)

def play_word(player, word):
  result = player_to_words[player] = word
  return result
#Above, this adds a new player and their words to the list

play_word("Jerry", ["BROAD, JAMS, CHOOSE"])

print()
print(player_to_words)

def update_point_totals(player, word_played):
  points = score_word(word_played)
  if player not in player_to_points:
    player_to_points[player] = 0
  player_to_points[player] += points


update_point_totals("player1", "DREAMS")

print()
print(player_to_points)


