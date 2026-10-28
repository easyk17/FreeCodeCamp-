import datetime
import random

log_messages = [
    "User logged in",
    "User logged out",
    "Error occurred",
    "Success occurred",
    "Invalid input",
    "System update available",
    "New feature added",
    "Bug fixed",
    "System crashed",
    "User not found"
]

def generate_logs(num_logs=10000):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=30)
    logs = []
    
    for _ in range(num_logs):
        random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
        random_date = start_date + datetime.timedelta(seconds=random_seconds)
        timestamp = random_date.strftime("%Y-%m-%d %H:%M:%S")
        message = random.choice(log_messages)
        logs.append(f"{timestamp} - {message}")
        
    logs.sort()
    return logs

def write_to_file(logs, filename="logs.txt"):
    with open(filename, "w") as file:
        for log in logs:
            file.write(log + "\n")

if __name__ == "__main__":
    print("Generating 10,000 logs...")
    my_logs = generate_logs()
    write_to_file(my_logs)
    print("Logs generated and saved to logs.txt successfully!")