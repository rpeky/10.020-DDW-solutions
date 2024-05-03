

class RobotTurtle:
    #__init__ is used when creating an instance of a class - 'instantiation'
    #Define attributes objects in this class have under __init__ declaration
    #self - allows the function to access the attributes and methods within the class, no input
    #name - expected input (first one) when declaring the object - gives the object a name
    #speed = 1 - optional input, if no input is given, speed is set as 1, declaring a value after name (turtle1, 3) will change the value of speed
    def __init__(self, name, speed = 1):
        #python uses _ before the name of a variable to reference varibles to be used inside the class
        self._name = name
        self._speed = speed
        self._pos =(0,0)

    #method definition - functions you can call using the object
    def move(self, direction):
        #basic math to shift in the x or y direction by the speed set at the start
        update = {'up': (self._pos[0], self._pos[1] + self._speed),
                  'down': (self._pos[0], self._pos[1] - self._speed),
                  'left': (self._pos[0] - self._speed, self._pos[1]),
                  'right': (self._pos[0] + self._speed, self._pos[1])
                  }
        self._pos = update[direction]

    def tell_name(self):
        print(f"My name is {self._name}")


def main():
    #example of how to instantiate an object from the class RobotTurtle
    turtle_1 = RobotTurtle("turtle1")
    #call function to print the name of the turtle from the _name method - remember to access methods with () even with no input needed
    turtle_1.tell_name()
    #can access using ._name as well
    print(turtle_1._name)
    #show initial position of turtle, move turtle 1 unit up, show new position of turtle
    print("initial position: ", turtle_1._pos)
    turtle_1.move('up')
    print("new position: ", turtle_1._pos)



    #exmple of instantiating a turtle with a different speed
    turtle_fast = RobotTurtle("speedy_turtle", 10)
    turtle_fast.tell_name()
    print("initial position: ", turtle_fast._pos)
    turtle_fast.move('up')
    print("new position: ", turtle_fast._pos)


if __name__ == "__main__":
    main()
