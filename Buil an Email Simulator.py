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
# Step 13
# While users can send emails and have inboxes, a dedicated class is needed to manage inbox operations efficiently.
# The Inbox class will store a list of emails and provide methods to add new emails, list all emails, and manage them.
# Create a new class called Inbox with an __init__ method that initializes an empty list called emails.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 14
# Now it's time to connect the User and Inbox classes so that emails can actually be delivered!
# Users need to have proper Inbox objects instead of simple lists, and the send_email method should deliver emails to the receiver's inbox.
# Update the User class __init__ in a way that each user gets an actual Inbox object instead of an empty list created earlier.
# #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 15
# Your inbox needs a way to receive new emails. When someone sends an email to a user, it should be added to their inbox.
# Add a method called receive_email to your Inbox class that takes self and an email object email as parameters. Within the method body, add the email to the emails list using the append method.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 16
# Still within the send_email method, call the receive_email method of the receiver's inbox to add email to the receiver's inbox.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 17
# Now it's time to test the complete email system! Create two users and see the email functionality in action.
# Create two User objects: alice with name "Alice" and bob with name "Bob". This will demonstrate how users can be created and interact with each other.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 18
# Have Alice send an email to Bob to see if the email delivery works correctly.
# Use Alice's send_email method to send Bob an email with subject "Hello" and body "Hi Bob, how are you?".
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Step 19
# Now verify that the email was delivered successfully by printing the length of Bob's inbox emails.
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
        self.inbox = Inbox()  # Each user has an inbox to store received emails

    def send_email(self, receiver, subject, body):
        email=Email(self, receiver, subject, body)
        receiver.inbox.receive_email(email)  # Deliver the email to the receiver's inbox
class Inbox:
    def __init__(self):
        self.emails = []  # Initialize an empty list of emails
    def receive_email(self, email):
        self.emails.append(email)  # Add the email to the inbox

alice = User("Alice")
bob = User("Bob")
alice.send_email(bob, "Hello", "Hi Bob!")
print(len(bob.inbox.emails))  # Verify that the email was delivered successfully