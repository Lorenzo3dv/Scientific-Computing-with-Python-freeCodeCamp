import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        balls = []
        for i in range(number):
            tmp = random.randrange(0, len(self.contents))
            balls.append(self.contents.pop(tmp))
        return balls
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(0, num_experiments):
        copyhat = copy.deepcopy(hat)
        balls = copyhat.draw(num_balls_drawn)
        dict = {}
        for ball in balls:
            v = dict.get(ball, 0)
            dict[ball] = v + 1

        founds = True
        for b, v in expected_balls.items():
            if dict.get(b, 0) < v:
                founds = False
                break

        if founds:
            success += 1

    return success / num_experiments