import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.temp = []
        for i in kwargs:
            self.contents.extend([i] * kwargs[i])
        self.temp = self.contents.copy()

    def draw(self, num_balls):
        balls_drawn = []
        if num_balls >= len(self.contents):
          return self.contents
        for _ in range(num_balls):
            x = random.randint(0, len(self.contents) - 1)
            balls_drawn.append(self.contents.pop(x))
        return balls_drawn
    
    def reset(self):
      self.contents = self.temp.copy()

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    correct_count = 0

    for _ in range(num_experiments):
        balls_drawn = hat.draw(num_balls_drawn)
        for x in expected_balls:
            if balls_drawn.count(x) < expected_balls[x]:
                break
        else:
            correct_count += 1
        hat.reset()
    return correct_count / num_experiments
    