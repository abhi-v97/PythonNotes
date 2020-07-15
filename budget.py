class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def deposit(self, amount, desc=""):

        self.ledger.append({'amount': amount, 'description': desc})
        self.balance += amount

    def withdraw(self, amount, desc=""):

        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": desc})
            return True
        else:
            return False

    def transfer(self, amount, cat1):
        if self.withdraw(amount, "Transfer to " + cat1.name):
            cat1.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def __str__(self):

        x = '{:*^30}'.format(self.name) + "\n"

        for i in self.ledger:
          x += i["description"][:23].ljust(23) + \
                                           str("{:.2f}".format(
                                               i["amount"]).rjust(7)) + "\n"

        x += "Total: " + str(self.balance)

        return x


def create_spend_chart(categories):
    line1 = "Percentage spent by category"
    print(line1)
    names = []
    expenses = []
    percentage = []


    for i in categories:
        names.append(i.name)
        
        part = 0
        for j in i.ledger:
            if j["amount"] < 0:
                part += j["amount"]
        expenses.append(round(part, 2))

    
    for i in range(len(expenses)):
        percentage.append(expenses[i] / sum(expenses) * 100)
    print(percentage)
        

    i = 100
    row = ""
    maxlen = max(len(x.name) for x in categories)
    

    for i in range(100, -10, -10):

        row += str(i).rjust(3) + "|"
        

        for j in percentage: # credit zaneaw
            
            if j >= i:
                row += " o "
            else:
                row += "   "
        
        row += " \n"
    
    row += "    " + "-" * len(names) * 3 + "-" + "\n"
    
    
    for i in range(maxlen):
        row += "    "

        for j in categories:
            if i < len(j.name):
                row += " " + j.name[i] + " "
            else:
                row += "   "
    
        row += " \n"
  
    chart = row.rstrip() + "  "

    y = line1 + "\n" + chart

    print(y)

    return y




food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

create_spend_chart([business, food, entertainment])

