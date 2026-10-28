# Step 1: File read karo
def load_logs(filename="logs.txt"):
    with open(filename, 'r') as file:
        return file.readlines()

# Step 2: Binary Search function banao
def binary_search(logs, target):
    low = 0
    high = len(logs) - 1
    
    while low <= high:
        mid = (low + high) // 2
        log_timestamp = logs[mid].split(" - ")[0].strip()
        
        if log_timestamp == target.strip():
            return mid
        elif log_timestamp < target.strip():
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # <--- YEH LINE MISSING THI

# Step 3: Main function
def main():
    logs = load_logs()
    target = input("Enter timestamp to search (YYYY-MM-DD HH:MM:SS): ")
    
    # Yahan se neeche wali saari extra lines delete kar di hain
    result = binary_search(logs, target)
    
    if result != -1:
        print(f"Log found at line {result + 1}: {logs[result].strip()}")
    else:
        print("Log not found.")

if __name__ == "__main__":
    main()