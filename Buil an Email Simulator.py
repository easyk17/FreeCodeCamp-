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
# Step 5
# Emails should track whether they've been read or not. 
# Add a read attribute to the __init__ method and set it to False by default, since new emails start as unread.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 6
# Now test that the read attribute was added correctly to your Email class. 
# Since you already have an email object from the previous steps, print the read attribute to see that it's now False by default.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 7
# Now you'll add a method to mark an email as read. When someone opens an email, you want to change its status from unread to read. 
# This method will be simple - it just needs to set the read attribute to True.
# Add a method called mark_as_read to your Email class. This method should take only self as a parameter and set the read attribute to True.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 8
# Now, test the mark_as_read method you created in the Email class. Use the method on the existing Email object email_obj to change the status. 
# After marking the email as read, print the read attribute of email_obj to confirm the change.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 9
# Remove the email_obj and the following print statements.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 10
# Now that you have an initial setup of the Email class, it's time to create users who can send and receive emails. 
# Each user will have a name and will be able to perform email operations.
# Create a User class with an __init__ method that takes self and name as parameters. Within the class, assign the name parameter to self.name.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 11
# The User class needs a method to send emails to other users. When sending an email, you'll create a new Email object and add it to the receiver's inbox.
# Create a method called send_email in your User class. This method should take parameters for receiver, subject, and body.
# Inside the method, create a new Email object with the following parameter values and assign it to a variable named email:
# sender: self (the current user)
# receiver: receiver (the user receiving the email)
# subject: subject (the subject of the email)
# body: body (the body of the email)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 12
# Now that users can send emails, they need a way to store emails they receive. Each user should have an inbox to collect their emails.
# Add an inbox attribute to the User class __init__ method and initialize it as an empty list []. This will store all emails that the user receives.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False  # New emails start as unread
    def mark_as_read(self):
        self.read = True  # Mark the email as read

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = []  # Initialize an empty inbox
    def send_email(self, receiver, subject, body):
        email=Email(self, receiver, subject, body)
