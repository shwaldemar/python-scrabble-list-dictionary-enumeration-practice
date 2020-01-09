letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
  key:value
  for key,value
  in zip(letters, points)
}

letter_to_points[" "] = 0
print("list letter to points contains scrabble letters and their relative point scores:", letter_to_points)
print()

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)

    # point_total += letter_to_points[letter]

    # for key, value in letter_to_points.items():
    #   if letter.upper() == key:
    #     point_total += value

  return point_total

brownie_points = score_word("BROWNIE")

print("scrabble score for the word brownie:", brownie_points)
print()

player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

print("dictionary player to words contains players and lists of their words:", player_to_words)
print()

player_to_points = {}

def update_point_totals():
  for key,value in player_to_words.items():
    player_points = 0
    for i in value:
      player_points += score_word(i)
      player_to_points[key] = player_points
  return player_to_points

print("dictionary player to points contains players and the total points for their words:", update_point_totals())
print()

def play_word(player, word):
  player_to_words[player].append(word)
  return update_point_totals()

print("Updated scores after player1 adds CODE:", play_word("player1", "CODE"))

print()

print("Updated player words after player1 adds CODE:", player_to_words)
