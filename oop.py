#what is object oriented programming?
# is about creating objects that contain  both data and methods.
#OOP classes
#A Class is like an object constructor, or a "blueprint" for 
#creating objects.
#How to create a class.use the key word class
#create a user class with properties name,age,location
class User:
    def __init__(self, name, age, location):#__int__ initializes the users name,age and location
        self.name = name
        self.age = age
        self.location = location

    def display_user_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def print_location(self):
        print(f"Location: {self.location}")
      
# Create a User instance
user1 = User("Fortunate Gloria", 27, "Kampala")

# Access and display user's information
user1.display_user_info()

# Print the user's location using the method
user1.print_location()



