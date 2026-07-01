from struct import unpack


step 5
# Following the same structure you used in the previous steps, 
# the medical_records list has been filled up for you with other patients' data. 
# Feel free to take a look at it. Next you'll start to write the function to validate the data set. 
# Create a function named validate with a single parameter data. 
# You want to ensure that your data is either a list or a tuple. 
# Therefore, within the validate function, declare a variable named is_sequence and assign it a call to isinstance. 
# Pass in data as the first argument and a tuple containing list and tuple as the second argument.
# --------------------------------------------------------------------------------------------------------------------
#Step 6
#Create an if statement. For its condition, use the not operator to negate is_sequence. 
# Within the if statement, print Invalid format: expected a list or tuple. and return False.

# --------------------------------------------------------------------------------------------------------------------
# Step 7
# Right after your if statement, declare a variable named is_invalid and set it to False. 
# Later on, you'll use it as a flag to run a conditional statement.

# --------------------------------------------------------------------------------------------------------------------
# Step 8
# Create a for loop that iterates over data. 
# Use the enumerate function to get both the index and the item in data at each iteration. 
# Use index and dictionary as iteration variables.
# For now use pass to fill the loop body.

# --------------------------------------------------------------------------------------------------------------------
# Step 9
# You are checking if the data passed to your function is a list or a tuple. 
# You still need to ensure that each item in the sequence is a dictionary.
# Inside your for loop, if the item in dictionary is not an instance of dict, 
# print Invalid format: expected a dictionary at position <index>. 
# (where <index> should be replaced by the current index) and set is_invalid to True.

# --------------------------------------------------------------------------------------------------------------------
# Step 10
# After your for loop, still inside the validate function, create an if statement. 
# If is_invalid is True, return False.

# --------------------------------------------------------------------------------------------------------------------
# Step 11
# After the if statement, print the string Valid format.. Then return True.

# --------------------------------------------------------------------------------------------------------------------
# Step 12
# At the bottom of your code, call the validate function with medical_records as the argument.
# You should see Valid format. printed to the terminal.

# --------------------------------------------------------------------------------------------------------------------
# Step 13
# To test the first if statement of your function, turn medical_records into a string. 
# You should see Invalid format: expected a list or tuple. printed to the terminal. 
# (in freecodecamp they used """ .....""" to turn it into a string, but you can also use single or double quotes). AI showed str () function to turn it into a string.

# --------------------------------------------------------------------------------------------------------------------
# Step 14
# Now turn medical_records back to a list/tuple of dictionaries.

# --------------------------------------------------------------------------------------------------------------------
# Step 15
# To test the second conditional statement, add two items of your choice that are not dictionaries at the end of the medical_records list. 
# You should see two validation messages printed to the terminal.

# --------------------------------------------------------------------------------------------------------------------
# Step 16
# Now that you tested the validation for this part, remove the last two items from the medical_records list.

# --------------------------------------------------------------------------------------------------------------------
# Step 17
# As you learned in a previous lesson, a set is an unordered collection of unique elements:
# Example Code
# integers = set([3, 5, 1, 2, 1, 3, 4])
# print(integers) # {1, 2, 3, 4, 5}
# You're going to use a set to ensure that each dictionary does not contain extra or misspelled keys.
# Inside the validate function, use the set() constructor to create a set from the following list of keys that each dictionary should have: 
# ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']. Assign the set to a variable named key_set.

# --------------------------------------------------------------------------------------------------------------------
# (Step 18
# The keys() method returns a view object containing all the keys from doctest import Example from a dictionary:

# Example Code
        # person = {
        # 'name': 'John',
        # 'age': 33 }
            # print(person.keys()) # dict_keys(['name, 'age'])

# Inside your for loop, after the first if statement, create an if statement that runs when the set of keys from the current dictionary is different from key_set. 
# This is to ensure that no missing or invalid keys are present in the dictionary.
# Within the new if statement, print Invalid format: <dictionary> at position <index> has missing and/or invalid keys. 
# (where <dictionary> and <index> should be replaced by the dictionary and index at the current iteration) and set is_invalid to True.

# --------------------------------------------------------------------------------------------------------------------
# Step 19
# To test that everything is working correctly, try to comment out the age key from the first dictionary in medical_records.
# You should see a validation message appear in the terminal.

# --------------------------------------------------------------------------------------------------------------------
# Step 20
# Now restore the line 'age': 34,.

# --------------------------------------------------------------------------------------------------------------------
# Step 21
# Now you are going to make the validation more granular. 
# Create a function named find_invalid_records to find invalid values in a dictionary. 
# Give it the following parameters: patient_id, age, gender, diagnosis, medications, last_visit_id.
# Inside your new function, create an empty dictionary named constraints. 
# Then, return constraints from your new function.

# --------------------------------------------------------------------------------------------------------------------
# # Step 22
# The ** operator can be used to unpack the elements in a dictionary and 
# pass them as keyword arguments in a function call:

# Example Code
# def sum(a, b, c):
#     return a + b + c
# nums = {'a': 2, 'b': 4, 'c': 1}

# print(sum(**nums)) # 7
# In the example above, sum(**nums) is equivalent to sum(a=2, b=4, c=1).
# At the bottom of your code, print the result of calling the find_invalid_records function. 
# For its arguments, use the ** operator to unpack medical_records[0].

# --------------------------------------------------------------------------------------------------------------------
# Step 23
# The constraints dictionary will contain each key you should expect to have in the data to validate.
# The value associated to each of them will indicate the result of the validation.

# Add the key patient_id to the constraints dictionary. 
# For its value, use a call to isinstance passing in patient_id and str as the arguments.

# --------------------------------------------------------------------------------------------------------------------
# Step 24
# As you wrote in the previous step, patient_id should be a string. 
# You want to check that it also has a specific pattern though.
# For that, you are going to use a regular expression. 
# Therefore, at the top of your code, use the import keyword to import the re module.

# --------------------------------------------------------------------------------------------------------------------
# Step 25
# A regular expression, or regex, is a pattern used to match a sequence of characters in text. 
# The search function from the re module takes a regex pattern and a string as its arguments.

# It returns a corresponding match object if the pattern produces a match. Otherwise it returns None.

# Example Code
# import re

# greeting = "Hello there!"
# print(re.search('Hi', greeting)) # None
# print(re.search('Hello', greeting)) # <re.Match object; span=(0, 5), match='Hello'>
# Call re.search with the string p as the first argument and patient_id as the second argument. Use the and operator to add the function call as a second expression to the value of your patient_id key.

# --------------------------------------------------------------------------------------------------------------------
# Step 26
# Now you can see {'patient_id': None} printed to the terminal because the lowercase p does not match P1001 and the and operator returns the first falsy value of the expression.

# You want to ensure that the patient ID starts with the letter p, but it can be either lowercase or uppercase. To modify the matching behavior of regular expressions, you can use flags. For example, re.search accepts a third argument to specify any flags:

# Example Code
# import re

# greeting = "Hello there!"
# print(re.search('hello', greeting)) # None

# print(re.search('hello', greeting, re.IGNORECASE))
# <re.Match object; span=(0, 5), match='Hello'>
# Add re.IGNORECASE as the third argument to your re.search call. This will make your regex search case insensitive.

# After that, you'll see None replaced by the match object <re.Match object; span=(0, 1), match='P'>, where match indicates the match and span indicates its location in the string.

# --------------------------------------------------------------------------------------------------------------------
# # Step 27
# Regular expressions can contain special sequences consisting in a backslash (\) followed by a character. These sequences have a special meaning. For example, \d matches a decimal digit.

# Example Code
# import re

# book = "Fahrenheit 451"
# print(re.search('\d', book))
# # <re.Match object; span=(11, 12), match='4'>
# After the letter p, patient_id should have a series of numbers. So, modify your regex pattern to have the character p followed by the special sequence \d.

# --------------------------------------------------------------------------------------------------------------------
# # Step 28
# Quantifiers are used in regular expressions to specify how many times a character can be repeated. For example, the + character matches the previous character one or more times:

# Example Code
# import re

# book = "Fahrenheit 451"
# print(re.search('\d', book))
# # <re.Match object; span=(11, 12), match='4'>

# print(re.search('\d+', book))
# # <re.Match object; span=(11, 14), match='451'>
# So append a + quantifier to your regex pattern to match one or more digits.

# --------------------------------------------------------------------------------------------------------------------
# # Step 29
# Now that your regex matches the letter p followed by one or more digits, one last thing you need to check is that no extra characters are found in the string.

# To do that you can make use of another function from the re module. The fullmatch function returns a match object when the regex pattern matches the entire string and None otherwise.

# Example Code
# import re

# book = "Fahrenheit 451"
# print(re.fullmatch('\d+', book)) #None

# print(re.fullmatch('Fahrenheit \d+', book))
# # <re.Match object; span=(0, 14), match='Fahrenheit 451'>
# Replace the search call with a fullmatch call keeping the same arguments.
# --------------------------------------------------------------------------------------------------------------------
# Step 30
# Next, you want to verify that age is an integer. So add another key age to the constraints dictionary. 
# For its value, call isinstance passing age and int as its arguments.
# --------------------------------------------------------------------------------------------------------------------
# Step 31
# age should not only be a integer, it should be a positive integer greater than or equal to 18.
# Using the and operator, add a second expression to the value of the age key to check that.
--------------------------------------------------------------------------------------------------------------------
# Step 32
# Add another key gender to the constraints dictionary. 
# Following the format of the expression you wrote in the previous steps, verify that gender is a string. 
# Then, use the and operator to check that the lowercase gender is in ('male', 'female').
# --------------------------------------------------------------------------------------------------------------------
# Step 33
# Now add a key diagnosis to the constraints dictionary. 
# For its value, write an expression that checks that diagnosis is either an instance of str or is None.
# --------------------------------------------------------------------------------------------------------------------
# Step 34
# Next, add a medications key to the constraints dictionary. 
# For its value use isinstance to check that medications is a list.
# --------------------------------------------------------------------------------------------------------------------
# Step 35
# As you learned in a previous lesson, a list comprehension can be used to create a list starting from an existing iterable:

# Example Code
# squares = [0, 1, 4, 9, 16, 25]

# roots = [i ** 0.5 for i in squares]
# print(roots) # [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
# Each item in the medications list should be a string. In this step and the next one you'll write an expression to check that. 
# Use the and operator to add another expression to the value of the medications key.
# On the right side of the and operator, use the list comprehension syntax to create a list made by evaluating isinstance(i, str) for each i in medications.

# --------------------------------------------------------------------------------------------------------------------
# Step 36
# The all function returns True if all the elements from the iterable passed to it are truthy, and False otherwise:

# Example Code
# truthy = [1, 2, 3]
# print(all(truthy)) # True

# falsy = [0, 1, 2, 3]
# print(all(falsy)) # False
# Pass the list [isinstance(i, str) for i in medications] to the all function to ensure that every element in it is a string.


# --------------------------------------------------------------------------------------------------------------------
# Step 37
# Add one last key last_visit_id to the constraints dictionary. For its value, use isinstance to verify that last_visit_id is a string.

# --------------------------------------------------------------------------------------------------------------------
# Step 38
# It's time to use another regular expression. Similarly to what you've already done, use the and operator to add an expression to the current value of constraints['last_visit_id'].
# On the right side of the and operator, use the fullmatch function from the re module to ensure that last_visit_id starts with the letter v (either lowercase or uppercase) followed by one or more digits.

# --------------------------------------------------------------------------------------------------------------------
Step 39
# Now that your constraints dictionary is complete, you'll change the return statement of find_invalid_records to make it return a list of the invalid keys.
# Using the list comprehension syntax, return a list that evaluates key for each key, value in constraints.items().
# --------------------------------------------------------------------------------------------------------------------

# Step 40
# List comprehensions also accepts if clauses to filter out items from an iterable:

# Example Code
# nums = [1, 2, 3, 4, 5, 6]
# even_nums = [num for num in nums if num % 2 == 0]
# print(even_nums) # [2, 4, 6]
# Since you want to return a list containing only invalid keys, add an if clause to your comprehension so that each key is added to the list only when value is falsy.
# --------------------------------------------------------------------------------------------------------------------
# Step 41
# The find_invalid_records function is complete. Now, remove print(find_invalid_records(**medical_records[0])) from your code.

# --------------------------------------------------------------------------------------------------------------------
# Step 42
# Going back to the validate function, after the two if statements and still inside the for loop, create a variable named invalid_records.
# Then, assign it a call to find_invalid_records using the ** operator to unpack dictionary.
# --------------------------------------------------------------------------------------------------------------------

# Step 43
# If you pass invalid data to the validate function, for example a list containing non-dictionary elements or dictionaries with missing and/or invalid keys, 
# Python will raise an AttributeError and a TypeError, respectively. 
# Feel free to verify it by modifying the medical_records list.
# To avoid that, after setting is_invalid to True, use the continue keyword to skip to the next iteration in both your if statements.

# --------------------------------------------------------------------------------------------------------------------
# Step 44
# Right after the invalid_records variable, create a for loop to iterate over it. For each invalid record, print Unexpected format '<key>: <val>' at position <index>.. Replace <key>, <val>, and <index> with the current key, value, and index.
# Remember that invalid_records is a list of keys that refer to invalid records in the current dictionary. You will need to take the key from invalid_records and look up the value in dictionary.
# Position or index refers to the current dictionary in medical_records, defined by the outer for loop in the function.
# Review your code so far if you need to remind yourself of the loops and variables already created.
# Then, set is_invalid to True.
# Feel free to test the validate function with invalid data to see the validation messages.
# With that, the medical validator workshop is complete.
# --------------------------------------------------------------------------------------------------------------------

import re
medical_records = """[
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
    }"""
    
]
def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id, str) and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        'age': isinstance(age, int) and age >= 18,
        'gender: isinstance(gender, str) and gender.lower() in ('male', 'female'),
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list) and all([isinstance(i, str) for i in medications]),
        'last_visit_id': isinstance(last_visit_id, str) and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }
    return [key for key, value in constraints.items() if not value]

def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True
            continue
        if set(dictionary.keys()) != key_set:
            print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
            is_invalid = True
            continue
        invalid_records = find_invalid_records(**dictionary)
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True 

    if is_invalid:
        return False
    print("Valid format.")
    return True

validate(medical_records)
