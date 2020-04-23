class Robot:
    def __init__(self, name, colour, weight):
        self.name = name
        self.colour = colour
        self.weight = weight

    def introduce_self(self):
        print("My name is", self.name)

r1=Robot("Tom", "red", 30)
#r1.name="Tom"
#r1.colour="red"
#r1.weight=30

r1.introduce_self()


r2=Robot("Malcolm", "blue", "23")
#r2.name="Malcolm"
#r2.colour="blue"
#r2.weight=23

r2.introduce_self()
