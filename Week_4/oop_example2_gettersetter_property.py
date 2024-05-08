
class RobotTurtle2:
    def __init__(self, name, speed = 1):
        #note that name and speed dont have an underscor ein front anymore
        self.name = name
        self.speed = speed
        self._pos = (0,0)

    #property deorator - changes method of name (def name) into a getter method for this property name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str) and value != "":
            self._name = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if isinstance(value,int) and value > 0:
            self._speed = value

    @property
    def pos(self):
        return self._pos

    def move(self, direction):
        update = {'up' : (self.pos[0], self.pos[1] + self.speed),
                  'down' : (self.pos[0], self.pos[1] - self.speed),
                  'left' : (self.pos[0] - self.speed, self.pos[1]),
                  'right' : (self.pos[0] + self.speed, self.pos[1])
                  }
        self._pos = update[direction]

    def tell_name(self):
        print(f"My name is {self.name}")



def main():
    turtle1 = RobotTurtle2("t1")
    print(turtle1.name)
    print(turtle1.speed)
    turtle1.name = 12
    turtle1.speed = "Aaaaaaaa"
    print(turtle1.name)
    print(turtle1.speed)
    print(turtle1.pos)
    turtle1.move("up")
    print(turtle1.pos)

if __name__ == "__main__":
    main()
