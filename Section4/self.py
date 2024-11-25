# Self demo
#Programmer: Matthew Washburn
class food:
    def __init__(self, fruit, color):
        self.fruit =  fruit
        self.color = color

    # Define show()
    def show(self):
        print('fruit is', self.fruit)
        print('color is', self.color)

# Create two objects
apple = food('apple', 'red')
grape = food('grapes', 'green')

# Display each object's fields, namely fruit and color
apple.show()
grape.show()


