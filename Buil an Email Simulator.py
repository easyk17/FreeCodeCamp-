# Step 1
# In this workshop, you are going to build an Email Simulator that simulates sending, receiving, and managing emails between different users. 
# You'll learn about classes, objects, and how to organize code in an object-oriented way.
# Begin by creating a class named Email using the class keyword.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 2
# Your Email class needs to store information about each email when it's created.
# Inside your Email class, remove the existing pass keyword and create the __init__ method that takes self, sender, receiver, subject, and body as parameters.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 3
# Inside the __init__ method, you need to assign the parameter values to the object's attributes so each email can store its information.
# Inside your __init__ method, remove the pass keyword and assign the parameters to self.sender, self.receiver, self.subject, and self.body.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 4
# Now test the Email class by creating an email object and checking that it stores information correctly. You'll print a couple of attributes to verify everything works.
# Create an email object named email_obj with alice@example.com as the sender, bob@example.com as the receiver, Hello as the subject, and Hi Bob! as the body. 
# Then print the sender and subject attributes as separate print statements to verify they are stored correctly.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Email:
    def__init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
email_obj = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob!")
print(email_obj.sender)
print(email_obj.subject)
