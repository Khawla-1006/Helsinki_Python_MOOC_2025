# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        payment_status = False
        if amount <= self.balance :
             self.balance -= amount
             payment_status = True
        return payment_status
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        change = payment
        if payment > 2.50 :
            change -= 2.5 
            self.funds += 2.5
            self.lunches += 1
        return change
            


    def eat_special(self, payment: float):
         # A special lunch costs 4.30 euros.
         # Increase the value of the funds at the terminal by the price of the lunch,
         # increase the number of specials sold, and return the appropriate change.
         # If the payment passed as an argument is not large enough to cover the price,
         # the lunch is not sold, and the entire sum is returned.
         change = payment
         if payment > 4.30 :
             change -= 4.30 
             self.funds += 4.30
             self.specials += 1
         return change

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        card_status = False
        if card.balance >= 2.5 :
            card.balance -= 2.5 
            card_status = True
            self.lunches += 1
        return card_status

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        card_status = False
        if card.balance >= 4.30 :
            card.balance -= 4.30 
            card_status = True
            self.specials += 1
        return card_status

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount

if __name__ == "__main__":
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)

    exactum = PaymentTerminal()
    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)
