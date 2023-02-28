import random

class Person:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moves = 0
    
    def move(self):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.x += dx
        self.y += dy
        self.moves += 1

class Game:
    def __init__(self, width, height, num_people):
        self.width = width
        self.height = height
        self.num_people = num_people
        self.people = []
        self.steps = 0
        for i in range(num_people):
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
            self.people.append(Person(x, y))
    
    def check_collisions(self):
        for i in range(self.num_people):
            for j in range(i+1, self.num_people):
                if self.people[i].x == self.people[j].x and self.people[i].y == self.people[j].y:
                    return True
        return False
    
    def run(self):
        while not self.check_collisions():
            for person in self.people:
                person.move()
            self.steps += 1
        return self.steps
    
    def reset(self):
        self.people = []
        self.steps = 0
        for i in range(self.num_people):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            self.people.append(Person(x, y))

# Example usage:
game = Game(5, 5, 2)
steps = game.run()
print(f"Game took {steps} steps to complete")
game.reset()
