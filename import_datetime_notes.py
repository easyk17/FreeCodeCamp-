import datetime  # Import the datetime module to work with timestamps

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()  # Add a timestamp for when the email was created
        self.read = False  # New emails start as unread

    def mark_as_read(self):
        self.read = True  # Mark the email as read

    def display_full_email(self):
        self.mark_as_read()  # Mark the email as read when displaying it        
        print("\n--- Email ---")
        print(f"From: {self.sender.name}")  # Display the sender's name
        print(f"To: {self.receiver.name}")  # Display the receiver's name
        print(f"Subject: {self.subject}")  # Display the subject of the email
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")  # Display the timestamp
        print(f"Body: {self.body}")  # Display the body of the email
        print('------------\n')

    def __str__(self):
        status = 'Read' if self.read else 'Unread'  # Determine the read status     
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    
class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()  # Each user has an inbox to store received emails

    def send_email(self, receiver, subject, body):
        email = Email(self, receiver, subject, body)
        receiver.inbox.receive_email(email)  # Deliver the email to the receiver's inbox
        print(f"Email sent from {self.name} to {receiver.name}!\n")  # Confirmation message

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:")  # Personalized header
        self.inbox.list_emails()  # List all emails in the user's inbox

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)


class Inbox:
    def __init__(self):
        self.emails = []  # Initialize an empty list of emails

    def receive_email(self, email):
        self.emails.append(email)  # Add the email to the inbox

    def list_emails(self):
        if not self.emails:
            print("Your inbox is empty.\n")  # Handle the case where the inbox is empty
            return
        
        # Fixed Indentation: Yeh lines ab list_emails ke andar hain
        print("\nYour Emails:")
        for i, email in enumerate(self.emails, start=1):
            print(f"{i}. {email}")  # Print the numbered list of emails
    
    def read_email(self, index):
        if not self.emails:
            print("Inbox is empty.\n")  # Handle empty inbox
            return
            
        # Fixed: 'actual.index' ko 'actual_index' kiya aur check ke niche laya
        actual_index = index - 1  
        
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")  # Handle invalid index
            return
        self.emails[actual_index].display_full_email()  # Display the full email content

    def delete_email(self, index):
        if not self.emails:
            print("Inbox is empty.\n")  # Handle empty inbox
            return
            
        actual_index = index - 1  # Convert 1-based index to 0-based index
        if actual_index < 0 or actual_index >= len(self.emails):
            print("Invalid email number.\n")  # Handle invalid index
            return
        del self.emails[actual_index]  # Delete the email at the given index
        print("Email deleted.\n")  # Confirmation message


def main():
    tory = User("Tory")  # Create a user named Tory
    ramy = User("Ramy")  # Create a user named Ramy
    
    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")  # Tory sends an email to Ramy
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")  # Ramy sends an email to Tory
    
    ramy.check_inbox()  # Ramy checks his inbox
    ramy.read_email(1)  # Ramy reads the first email
    ramy.delete_email(1)  # Ramy deletes the first email
    ramy.check_inbox()  # Ramy checks his inbox again to see the changes


if __name__ == '__main__':
    main()  # Call the main function to run the email simulator