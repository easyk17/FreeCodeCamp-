# step 5
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

