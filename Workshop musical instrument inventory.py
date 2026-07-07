# Step 1
# In this workshop, you'll get some practice with Python's classes and objects by building a musical instrument inventory.

# To define a class in Python, use the class keyword followed by the class name and a colon.

# Example Code
# class ClassName:
#     # class contents go here
# Remember that in Python, class names typically use PascalCase, which means each word starts with an uppercase letter with no spaces between words.

# # Start by creating a class called MusicalInstrument. Add pass as the body of the class for now.
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 2
# Methods are functions defined inside a class that can perform actions using the class's data. Here is how you create methods:

# Example Code
# def method_name(parameter1, parameter2,...):
#     # Method contents will go here
# In Python, the __init__ method is a special method known as the initializer method, which is called when you create a new instance of the class.

# Inside your MusicalInstrument class, add an __init__ method with three parameters: self, name, and instrument_type.

# The self parameter is a standard way to refer to the instance of the class and is required as the first parameter for all instance methods in a class.
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 3
# In the __init__ method, you need to assign the parameters to instance attributes. Instance attributes are variables that belong to a specific instance of a class.

# Inside your __init__ method, assign the name parameter to self.name and the instrument_type parameter to self.instrument_type.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 4
# Now it's time to create instances of your MusicalInstrument class.

# To create an instance of a class, you call the class name like a function, passing the required arguments for the __init__ method (except for self, which is automatically handled by Python).

# Example Code
# my_instance = ClassName(arg1, arg2)
# When you create this instance, Python calls your __init__ method and stores the values as instance attributes that belong only to this specific instance.

# Outside the class definition, create an instance named instrument_1 for an Oboe which is a woodwind instrument.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 6
# You can access the attributes of your instances using dot notation:

# Example Code
# instance_name.attribute_name
# This allows you to retrieve the values that were stored during initialization.

# Try printing the name and instrument_type attributes of both your instances. You'll be able to see the values you assigned when you created them.
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 7
# Now that you understand how to access object attributes, remove the existing print calls.
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 9
# Inside your play method, use print() to display a message about playing the instrument.

# Use an f-string to include the instrument's name in the message: The [instrument name] is fun to play!. The [instrument name] should be replaced with the actual name of the instrument.
# # # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Step 10
# Next, add another method to your class named get_fact that returns a fact about the instrument.

# This method should have only the self parameter and return an f-string that says The [instrument name] is part of the [instrument type] family of instruments.

# Unlike the play method which prints a message directly, this method should return a string that can be used elsewhere in your code.
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f"The {self.name} is fun to play!")

    def get_fact(self):
        return f"The {self.name} is part of the {self.instrument_type} family of instruments."

instrument_1 = MusicalInstrument("Oboe", "Woodwind")
instrument_2 = MusicalInstrument("Trumpet", "Brass")
