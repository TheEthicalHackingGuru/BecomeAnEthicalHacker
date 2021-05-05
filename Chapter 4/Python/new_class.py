
class Greeter:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("hi there! %s", self.name)
        

if __name__ == '__main__':
    g = Greeter("bob")
    g.greet()


# class defintitions cant be empty in python3
# class Greeter:
    # def __init__(self):
       # pass
        
        

# if __name__ == '__main__':
  #  g = Greeter("bob")
  #  g.greet()
