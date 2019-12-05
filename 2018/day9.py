
def play_game(players, victory_condition, known_max=None):
    print 'Starting a new game with {0} players until marble #{1}'.format(players, victory_condition)
    scores = [0] * players
    marble_id = 0
    current_marble = 0
    gameboard = [0]
    while True:
        for turn in range(0, players):
            marble_id += 1
            if marble_id % 1e6 == 0:
                print 'Hit millionth marble: {0}'.format(marble_id)
            points, current_marble = take_turn(marble_id, current_marble, gameboard)
            #print '[{0}]: [{2}]: {1}'.format(turn+1, gameboard, marble_id)
            scores[turn] += points
            if marble_id == victory_condition:
                print 'Max Score = {0}'.format(max(scores))
                return

def take_turn(marble_id, current_marble, gameboard):
    #print 'Placing marble #{0} at {1}'.format(marble_id, current_marble)
    if marble_id % 23 == 0:
        #print 'BACKWARDS! {0} / 23 = {1}'.format(marble_id, marble_id/23)
        current_marble = (current_marble - 7) % len(gameboard)
        score = marble_id + gameboard.pop(current_marble)
        return score, current_marble
    else:
        current_marble = (current_marble + 2) % len(gameboard)
        gameboard.insert(current_marble, marble_id)
        return 0, current_marble

#play_game(9, 25)
#play_game(17, 1104, 2764)
#play_game(10, 1618, 8317)
#play_game(30, 5807, 37305)
#play_game(21, 6111, 54718)
#play_game(13, 7999, 146373)

play_game(471, 72026)
#play_game(471, 72026*100)