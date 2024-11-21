import time

class Bank:
    WITHDRAWAL = 'Withdrawal'
    DEPOSIT = 'Deposit'
    INITIAL_BALANCE = 'Initial balance'

    def __init__(self, name: str, account_no: int, balance: float) -> None:
        self.name = name
        self.account_no = account_no
        self.balance = balance
        self.history = {f'{self.get_time()}': f'{self.INITIAL_BALANCE}: USD {self.balance}'}

    def format_time(self, timestamp) -> str:
        formatted_time = time.strftime('%H:%M:%S', time.localtime(timestamp))
        milliseconds = int((timestamp % 1) * 1000)
        return f'{formatted_time}.{milliseconds:03d}'

    def get_time(self) -> str:
        return self.format_time(time.time())
    
    def update_history(self, transaction_type: str, amount: float) -> None:
        time_stamp = self.get_time()
        self.history[time_stamp] = f'{transaction_type} USD {amount}. Balance: USD {self.balance}'

    def withdraw(self, amount: float) -> float:
        self.balance -= amount
        self.update_history(self.WITHDRAWAL, amount)
        return self.balance

    def deposit(self, amount: float) -> float:
        self.balance += amount
        self.update_history(self.DEPOSIT, amount)
        return self.balance

    def check_balance(self) -> str:
        return f'Balance is {self.balance}'

    def get_history(self) -> str:
        formatted_history = f'\nTRANSACTION HISTORY FOR ACC: {self.account_no} ({self.name})\n'
        for timestamp, details in self.history.items():
            formatted_history += f'- {timestamp}: {details}\n'
        return formatted_history
    
    def print_history(self):
        print(self.history)


david = Bank('David', 1234567890, 200)
wait = .1
print('balance', david.balance)
time.sleep(wait)

david.withdraw(50)
print('withdraw', david.balance)
time.sleep(wait)

david.withdraw(30)
print('withdraw', david.balance)
time.sleep(wait)

david.deposit(500)
print('deposit', david.balance)
time.sleep(wait)

david.deposit(5000)
print('deposit', david.balance)
time.sleep(wait)

print(david.check_balance())
print(david.get_history())