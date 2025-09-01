"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""

accounts = {}  
# accounts = {account_number: {"name": str, "balance": float, "overdraft_limit": float}}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    if account_number in accounts:
        return f"Account {account_number} already exists!"
    
    accounts[account_number] = {
        "name": name,
        "balance": kwargs.get("balance", 0.0),
        "overdraft_limit": kwargs.get("overdraft_limit", 0.0)
    }
    return f"Account for {name} created successfully."


def deposit(account_number, amount):
    """Deposit money into account."""
    if account_number not in accounts:
        return "Account not found!"
    
    accounts[account_number]["balance"] += amount
    return f"Deposited {amount} into {accounts[account_number]['name']}'s account."


def withdraw(account_number, amount):
    """Withdraw money if balance is sufficient. else: insufficient funds."""
    if account_number not in accounts:
        return "Account not found!"
    
    balance = accounts[account_number]["balance"]
    overdraft = accounts[account_number]["overdraft_limit"]
    
    if balance + overdraft >= amount:
        accounts[account_number]["balance"] -= amount
        return f"Withdrew {amount} from {accounts[account_number]['name']}'s account."
    else:
        return "Insufficient funds."


def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts if funds are sufficient."""
    if from_acc not in accounts or to_acc not in accounts:
        return "One or both accounts not found!"
    
    balance = accounts[from_acc]["balance"]
    overdraft = accounts[from_acc]["overdraft_limit"]
    
    if balance + overdraft >= amount:
        accounts[from_acc]["balance"] -= amount
        accounts[to_acc]["balance"] += amount
        return f"Transferred {amount} from {accounts[from_acc]['name']} to {accounts[to_acc]['name']}."
    else:
        return "Insufficient funds for transfer."

print("============Example usage============")
print(create_account(101, "Alice", balance=500))
print(create_account(102, "Bob", balance=300, overdraft_limit=100))

print(deposit(101, 200))
print(withdraw(101, 100))
print(transfer(101, 102, 400))

print(accounts)  # to see final balances

