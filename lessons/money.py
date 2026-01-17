class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Money object amount={self.amount}"

    def __eq__(self, other):
        if self.amount != other.amount:
            return False
        else:
            return True

money_igor = Money( 100)
money_nurbol = Money( 200)
print(money_igor)
print(money_nurbol == money_igor)
#print(money_nurbol  money_igor)