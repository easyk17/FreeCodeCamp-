# Build a Budget App
# In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should have a Category class that accepts a name as the argument.

# The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.

# The Category class should have the following methods:

# A deposit method that accepts an amount and an optional description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
# A withdraw method that accepts an amount and an optional description (default to an empty string). The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
# A get_balance method that returns the current category balance based on ledger.
# A transfer method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination], deposits it into the other category with description Transfer from [Source], where [Destination] and [Source] should be replaced by the name of destination and source categories. The method should return True when the transfer is successful, and False otherwise.
# A check_funds method that accepts an amount and returns False if it exceeds the balance or True otherwise. This method must be used by both the withdraw and transfer methods.
# When a Category object is printed, it should:

# Display a title line of 30 characters with the category name centered between * characters.
# List each ledger entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
# Show a final line Total: [balance], where [balance] should be replaced by the category total.
# Here is an example usage:

# food = Category('Food')
# food.deposit(1000, 'initial deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# print(food)
# And here is an example of the output:

# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96
# You should have a function outside the Category class named create_spend_chart(categories) that takes a list of categories and returns a bar-chart string. To build the chart:

# Start with the title Percentage spent by category.
# Calculate percentages from withdrawals only and not from deposits. The percentage should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
# Label the y-axis from 100 down to 0 in steps of 10.
# Use o characters for the bars.
# Include a horizontal line two spaces past the last bar.
# Write category names vertically below the bar.
# This function will be tested with up to four categories.

# Make sure to match the spacing of the example output exactly:

# Percentage spent by category
# 100|          
#  90|          
#  80|          
#  70|          
#  60| o        
#  50| o        
#  40| o        
#  30| o        
#  20| o  o     
#  10| o  o  o  
#   0| o  o  o  
#     ----------
#      F  C  A  
#      o  l  u  
#      o  o  t  
#      d  t  o  
#         h     
#         i     
#         n     
#         g     
# NOTE: open the browser console with F12 to see a more verbose output of the tests.

# Tests:
# Failed:1. The deposit method should create a specific object in the ledger instance variable.
# Failed:2. Calling the deposit method with no description should create a blank description.
# Failed:3. The withdraw method should create a specific object in the ledger instance variable.
# Failed:4. Calling the withdraw method with no description should create a blank description.
# Failed:5. The withdraw method should return True if the withdrawal took place.
# Failed:6. Calling food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread') should return a balance of 854.33.
# Failed:7. Calling the transfer method on a category object should create a specific ledger item in that category object.
# Failed:8. The transfer method should return True if the transfer took place.
# Failed:9. Calling transfer on a category object should reduce the balance in the category object.
# Failed:10. The transfer method should increase the balance of the category object passed as its argument.
# Failed:11. The transfer method should create a specific ledger item in the category object passed as its argument.
# Failed:12. The check_funds method should return False if the amount passed to the method is greater than the category balance.
# Failed:13. The check_funds method should return True if the amount passed to the method is not greater than the category balance.
# Failed:14. The withdraw method should return False if the withdrawal didn't take place.
# Failed:15. The transfer method should return False if the transfer didn't take place.
# Failed:16. Printing a Category instance should give a different string representation of the object.
# Failed:17. Title at the top of create_spend_chart chart should say Percentage spent by category.
# Failed:18. create_spend_chart chart should have correct percentages down the left side.
# Failed:19. The height of each bar on the create_spend_chart chart should be rounded down to the nearest 10.
# Failed:20. Each line in create_spend_chart chart should have the same length. Bars for different categories should be separated by two spaces, with additional two spaces after the final bar.
# Failed:21. create_spend_chart should correctly show horizontal line below the bars. Using three - characters for each category, and in total going two characters past the final bar.
# Failed:22. create_spend_chart chart should not have new line character at the end.
# Failed:23. create_spend_chart chart should have each category name written vertically below the bar. Each line should have the same length, each category should be separated by two spaces, with additional two spaces after the final category.
# Failed:24. create_spend_chart should print a different chart representation. Check that all spacing is exact. Open your browser console with F12 for more details.





class Category:
    pass

def create_spend_chart(categories):
    # 1. Title line
    chart = "Percentage spent by category\n"
    
    # 2. Har category ka total spend (withdrawals) nikalna
    spends = []
    for category in categories:
        total_spent = 0
        for item in category.ledger:
            # Sirf withdrawals calculate karne hain (amounts less than 0)
            # Dhyan rahe: transfer method bhi withdraw use karta hai, toh wo bhi negative hota hai
            if item['amount'] < 0:
                total_spent += abs(item['amount'])
        spends.append(total_spent)
        
    total_all_spends = sum(spends)
    
    # 3. Percentages calculate karna aur nearest 10 par round down karna
    percentages = []
    for spend in spends:
        if total_all_spends > 0:
            # Round down to nearest 10 (Jaise 66.6% -> 60%)
            percent = int((spend / total_all_spends) * 100 // 10) * 10
        else:
            percent = 0
        percentages.append(percent)
        
    # 4. Y-axis ke numbers (100 se 0) aur 'o' bars banana
    for i in range(100, -1, -10):
        # Y-axis label ko right-align karna 3 spaces ki width me (e.g., "100|", " 90|", "  0|")
        chart += f"{i:>3}|"
        
        # Har category ke liye check karna ki kya uska percentage 'i' se bada ya barabar hai
        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        # Har line ke baad ek extra trailing space aur new line
        chart += " \n"
        
    # 5. Horizontal line banana (2 spaces past the last bar)
    # 3 spaces numbers ke liye + 1 bar '|' ke liye + (3 spaces * number of categories) + 1 extra space
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # 6. Category ke names ko vertically niche print karna
    # Sabse lambe name ki length nikalna
    max_len = max([len(category.name) for category in categories])
    
    # Har character row ke liye loop chalana
    for r in range(max_len):
        chart += "    "  # Shuruat me 4 spaces ka gap
        for category in categories:
            if r < len(category.name):
                chart += f" {category.name[r]} "
            else:
                chart += "   "  # Agar naam khatam ho gaya toh khali spaces
        
        # Aakhiri row ke baad new line nahi aani chahiye (FreeCodeCamp ki strict requirement)
        if r < max_len - 1:
            chart += " \n"
        else:
            chart += " "  # Last line sirf ek space ke sath end hogi
            
    return chart   



class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        transaction = {'amount': amount, 'description': description}
        self.ledger.append(transaction)

        if not description:
            return ''

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            transaction = {'amount': -amount, 'description': description}
            self.ledger.append(transaction)
            return True
        else:
            return False

    
    def get_balance(self):
        total_balance = 0
        for transaction in self.ledger:
            total_balance += transaction['amount']
        return total_balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True 
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ''
        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = f"{transaction['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total