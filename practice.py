class Person:
    def __init__(self, age):
        self._age = age

    # @property #same as def get_age(self)
    # def age(self):
    #     print('getter method called')
    #     return self._age
    def get_age(self):
        return self._age

    # @age.setter
    # def age(self,new_age):
    #     print('calling setter')
    #     self._age=new_age
    #     if new_age>150:
    #         self.dead=True

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

#---------------------------------
# super() practice
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self,lenght):
        super().__init__(lenght,lenght)

class Cube(Square):
    def surface_area(self):
        return super().area() *6
    
    def volume(self):
        return super().area() * self.length