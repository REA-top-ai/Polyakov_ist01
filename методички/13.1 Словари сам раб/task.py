letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter: point for letter, point in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word,letter_to_points):
    score = 0
    for i in word.upper():
        score += letter_to_points.get(i,0)
    return score



player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],"wordNerd": ["EARTH", "EYES", "MACHINE"],"Lexi Con": ["ERASER", "BELLY", "HUSKY"],"Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def update_point_totals(player_to_words, letter_to_points):
    for player,words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word,letter_to_points)
        player_to_points[player] = player_points 
    return player_to_points

def play_word(player, word, player_to_words, letter_to_points):
    
    word = word.upper()

    if player in player_to_words:
        player_to_words[player].append(word)

    else:
        player_to_words[player] = [word]
    
    player_to_points = update_point_totals(player_to_words, letter_to_points)
    return player_to_points
