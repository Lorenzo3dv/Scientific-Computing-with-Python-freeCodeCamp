class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        to_print = self.category.center(30, "*") + "\n"
        for item in self.ledger:
            add_to_print = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            to_print += add_to_print + "\n"
        to_print += "Total: " + str(self.get_balance())
        return to_print
    
    def deposit(self, amount, description = ""):
        dict = {"amount": amount, "description": description}
        self.ledger.append(dict)

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            dict = {"amount": -amount, "description": description}
            self.ledger.append(dict)
            return True
        else:
            return False
        
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def transfer(self, amount, budget_category):
        
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budget_category.category)
            budget_category.deposit(amount, "Transfer from " + self.category)
            return True
        else: 
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent_in_each_category = []
    category_names = []
    
    #total amount for each category
    for category in categories:
        total_amount_category = 0
        category_names.append(category.category)
        for item in category.ledger:
            if item["amount"] < 0:
                total_amount_category += item["amount"]
        spent_in_each_category.append(total_amount_category)
    total_spent = sum(spent_in_each_category)

    #calculating percentages
    percentages = []
    for spent in spent_in_each_category:
        percentages.append(int(spent / total_spent * 100))

    #building bar chart
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) +"| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
        
    chart += "    " + "---" * len(categories) + "-" + "\n"

    max_name_length = max(len(name) for name in category_names)

    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart