'''Task: Find the Missing Number
Ek list di hai jisme 1 se N tak numbers hain,
but EK number missing hai.
Wo missing number dhundo.

Example:
Input:  [1, 2, 4, 5, 6]
Output: 3

Input:  [1, 3, 4, 5]
Output: 2
Rules:
Function banao → find_missing(numbers)
2 different approaches se solve karo
File save karo → mujhe path batao → main review karunga'''

def find_missing(numbers):
    # Approach 1: Using the sum formula
    n = len(numbers) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum
    return missing_number
print (find_missing([1, 2, 4, 5, 6]))  # Output: 3
print(find_missing([1, 3, 4, 5]))  # Output: 2