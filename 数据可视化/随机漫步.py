from random import choice
import matplotlib.pyplot as plt
class Walk():
    def __init__(self,numberpoint=100000):
        self.numberpoint = numberpoint
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        while len(self.x_value)<self.numberpoint:
            #方向
            x_which = choice([1,-1])
            #距离
            x_many = choice([0,1,2,3,4,5])
            x_move = x_which*x_many

            y_which = choice([1,-1])
            y_many = choice([0,1,2,3,4,5])
            y_move = y_many*y_which

            if x_move == 0 and y_move == 0:
                continue

            x_next = self.x_value[-1] + x_move
            y_next = self.y_value[-1] + y_move

            self.x_value.append(x_next)
            self.y_value.append(y_next)

            

w = Walk()
w.fill_walk()
point_numbers = list(range(w.numberpoint))
plt.figure(figsize=(10,6))
plt.scatter(w.x_value,w.y_value,c=point_numbers, cmap=plt.cm.Blues,edgecolor='none',s=1)
plt.scatter(0,0,c='green',edgecolor='none',s=15)
plt.scatter(w.x_value[-1],w.y_value[-1],c='red',edgecolor='none',s=15)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()

