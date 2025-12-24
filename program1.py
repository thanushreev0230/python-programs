class Dog:
    """class Dog is defind"""
    def bark(self):
        """Instance method"""
        print("Dog barking")
        print(id(self))
dog_one=Dog()
dog_one.bark()
print(id(dog_one))
