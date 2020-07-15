import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):

        self.contents = []
        for i in kwargs:
            for j in range(kwargs[i]):
                self.contents.append(i)

    def draw(self, num_balls_drawn):

        self.num_balls_drawn = num_balls_drawn
        x = []

        try:
            for i in range(num_balls_drawn):
                x.append(random.choice(self.contents))
                self.contents.remove(x[i])
        except IndexError:
            self.contents.append(x)

        return x



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        exp_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        
        for j in draw:
            if j in exp_balls_copy:
                exp_balls_copy[j] -= 1

        if(all(x <= 0 for x in exp_balls_copy.values())):
            m += 1

    return (m / num_experiments)
        


hat = Hat(blue=3, red=2, green=6)
probability = experiment(hat=hat, 
                  expected_balls={"blue":2,"green":1},
                  num_balls_drawn=4,
                  num_experiments=1000)
print("Probability:", probability)

hat =Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability =experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print(probability)