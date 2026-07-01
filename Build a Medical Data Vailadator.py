step 5
# Following the same structure you used in the previous steps, 
# the medical_records list has been filled up for you with other patients' data. 
# Feel free to take a look at it. Next you'll start to write the function to validate the data set. 
# Create a function named validate with a single parameter data. 
# You want to ensure that your data is either a list or a tuple. 
# Therefore, within the validate function, declare a variable named is_sequence and assign it a call to isinstance. 
# Pass in data as the first argument and a tuple containing list and tuple as the second argument.

#Step 6
#Create an if statement. For its condition, use the not operator to negate is_sequence. 
# Within the if statement, print Invalid format: expected a list or tuple. and return False.

# Step 7
# Right after your if statement, declare a variable named is_invalid and set it to False. 
# Later on, you'll use it as a flag to run a conditional statement.

# Step 8
# Create a for loop that iterates over data. 
# Use the enumerate function to get both the index and the item in data at each iteration. 
# Use index and dictionary as iteration variables.
# For now use pass to fill the loop body.

# Step 9
# You are checking if the data passed to your function is a list or a tuple. 
# You still need to ensure that each item in the sequence is a dictionary.
# Inside your for loop, if the item in dictionary is not an instance of dict, 
# print Invalid format: expected a dictionary at position <index>. 
# (where <index> should be replaced by the current index) and set is_invalid to True.

# Step 10
# After your for loop, still inside the validate function, create an if statement. 
# If is_invalid is True, return False.

# Step 11
# After the if statement, print the string Valid format.. Then return True.

# Step 12
# At the bottom of your code, call the validate function with medical_records as the argument.
# You should see Valid format. printed to the terminal.

# Step 13
# To test the first if statement of your function, turn medical_records into a string. 
# You should see Invalid format: expected a list or tuple. printed to the terminal.

# Step 14
# Now turn medical_records back to a list/tuple of dictionaries.

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False
    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False
    print("Valid format.")
    return True

validate(medical_records)

