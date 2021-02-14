# CHALLENGE 1

result = 0

calc_input = input('What calculation would you like to do? (add, sub, mult, div) ').lower()
n1 = int(input('What is number 1? '))
n2 = int(input('What is number 2? '))
if calc_input == 'add':
    result = n1 + n2
elif calc_input == 'sub':
    result = (n1 - n2)
elif calc_input == 'mult':
    result = (n1 * n2)
elif calc_input == 'div':
    result = (n1 / n2)
print(f'Your result is {result}')

# CHALLENGE 2

str_input = input('Enter a string: ')[::-1]
print(str_input)

# CHALLENGE 3        

class Account:
    def __init__(self):
        self.balance = 100

    def deposit(self, amt):
        self.balance = self.balance + amt
        return self.balance
    
    def withdraw(self, amt):
        self.balance = self.balance - amt
        return self.balance

    def check_balance(self):
        print('Your current balance is\n', self.balance)

def main():
    running = True
    account = Account()
    account.check_balance()
    while running:
        user_input = input('What would you like to do? (deposit, withdraw, check_balance)\n')
        if user_input == 'deposit':
            deposit_amt = int(input('How much would you like to deposit?\n'))
            account.deposit(deposit_amt)
            account.check_balance()
        elif user_input == 'withdraw':
            withdraw_amt = int(input('How much would you like to withdraw?\n'))
            account.withdraw(withdraw_amt)
            account.check_balance()
        elif user_input == 'check_balance':
            account.check_balance()

        user_input = input('Are you done?\n')
        if user_input == 'yes':
            running = False


main()