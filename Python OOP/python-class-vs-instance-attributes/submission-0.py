class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    acc_total = 0
    balance_acc = 0
    
    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance
        BankAccount.acc_total += 1
        BankAccount.balance_acc += balance
        pass


# TODO: Create two accounts
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${account1.balance}")
print(f"Bob's balance: ${account2.balance}")
print(f"Total Accounts: {BankAccount.acc_total}")
print(f"Total Balance: ${BankAccount.balance_acc}")


