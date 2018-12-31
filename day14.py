
class Board(object):
    def __init__(self, initial_state):
        self.recipes = [Recipe(item) for item in initial_state]
        self.count = len(self.recipes)
    
    def add(self, recipe):
        self.recipes.append(recipe)
        self.count += 1

class Elf(object):
    def __init__(self, starting_index):
        self.current_recipe = starting_index

class Recipe(object):
    def __init__(self, score):
        self.score = score

recipe_board = Board([3, 7])
jimmin = Elf(0)
marvin = Elf(1)
limit = '505961'
while recipe_board.count < int(limit) + 10:
    #scores = [' ' + str(r.score) + ' ' for r in recipe_board.recipes]
    #scores[jimmin.current_recipe] = scores[jimmin.current_recipe].replace(' ','+')
    #scores[marvin.current_recipe] = scores[marvin.current_recipe].replace(' ','#')
    for new_recipe in [int(score) for score in list(str(recipe_board.recipes[jimmin.current_recipe].score + recipe_board.recipes[marvin.current_recipe].score))]:
        recipe_board.add(Recipe(new_recipe))
    jimmin.current_recipe = (jimmin.current_recipe + recipe_board.recipes[jimmin.current_recipe].score + 1) % recipe_board.count
    marvin.current_recipe = (marvin.current_recipe + recipe_board.recipes[marvin.current_recipe].score + 1) % recipe_board.count
scores = [str(r.score) for r in recipe_board.recipes]
#scores[jimmin.current_recipe] = scores[jimmin.current_recipe].replace(' ','+')
#scores[marvin.current_recipe] = scores[marvin.current_recipe].replace(' ','#')
print ''.join(scores[int(limit):int(limit) + 10])

while str(limit) not in ''.join(str(r.score) for r in recipe_board.recipes):
    print 'Could not find. Increasing from {0} to {1}'.format(recipe_board.count, recipe_board.count + 100000)
    for _ in xrange(0, 100000):
        for new_recipe in [int(score) for score in list(str(recipe_board.recipes[jimmin.current_recipe].score + recipe_board.recipes[marvin.current_recipe].score))]:
            recipe_board.add(Recipe(new_recipe))
        jimmin.current_recipe = (jimmin.current_recipe + recipe_board.recipes[jimmin.current_recipe].score + 1) % recipe_board.count
        marvin.current_recipe = (marvin.current_recipe + recipe_board.recipes[marvin.current_recipe].score + 1) % recipe_board.count
print ''.join(str(r.score) for r in recipe_board.recipes).index(str(limit))