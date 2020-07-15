def round_to_nearest_ten(n):
  if n<10:
    return 0
  return round(n/10.0)*10


def create_spend_chart(categories):
    print("Percentage spent by category")

    withdrawls = []

  # used to find the category name with max length
    max_len_category = 0
    s=0

    for i in categories:

        amount_taken = 0

        for j in i.ledger:

            if j["amount"]<0:
                amount_taken +=-j["amount"]
                s+=(-j["amount"])
            
        if len(i.category)>max_len_category:
            max_len_category=len(i.category)
            withdrawls.append([i.category,amount_taken ])
        
    # used to calculate the percentage of a certain category
    for i in withdrawls:
        i.append(round_to_nearest_ten((i[1]/s)*100))
    
    s=""

    i = 100

    while i >= 0:
        
        # prints number and | symbol
        s+=str(i).rjust(3)+"|"+" "

        # loop for printing 'o' if the percentage>=t

        for j in range(len(withdrawls)):
            if withdrawls[j][2] >= i:
                s += "o"+"  "
            else:
                s += "   "
        i -= 10
        s+="\n"

    # adding '-' to the last lines
    s+="    "+("-"*10)+"\n"

    loop_var=0

    for i in range(max_len_category):
        s+="     "
        for j in range(len(withdrawls)):
        # checks whether a character exists at a length
            if len(withdrawls[j][0])-1<loop_var:
                # if no character exists adds empty string and 2 spaces
                s+="   "
            else:
                # adds character 
                s+=withdrawls[j][0][loop_var]+"  "
        loop_var+=1
        if i!=max_len_category-1:
            s+="\n"


    return s


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

actual = create_spend_chart([business, food, entertainment])
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
assertEqual(actual, expected, 'Expected different chart representation. Check that all spacing is exact.')