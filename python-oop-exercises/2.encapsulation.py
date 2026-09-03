"""
EXERCISE 2: Bank Account Vault
------------------------------
Requirements:
1. Create a class named 'BankAccount'.
2. In __init__, accept (account_holder, bank_branch, initial_balance) and set:
   - account_holder as public (no underscore)
   - _bank_branch as protected (one underscore: _)
   - __balance as private (two underscores: __)
3. Create a getter method 'get_balance(self)':
   - Returns the value of self.__balance.
4. Create a setter method 'set_balance(self, amount)':
   - If amount >= 0, update self.__balance = amount.
   - If amount < 0, print an error message "Error: Balance cannot be negative!".
5. Test your code:
   - Print the public account holder.
   - Attempt to access __balance directly inside a try/except block to catch the AttributeError.
   - Use get_balance() to read the balance.
   - Use set_balance() to update the balance safely.
"""


class BankAccount:

    def __init__(self, acc_holder, branch, balance):
        self.acc_holder = acc_holder
        self._branch = branch
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_bal):
        if new_bal>=0:
            self.__balance = new_bal
        else:
            print(f"Can't accept '{new_bal}'. Balance should be positive.")



# Testing ----------
acc1 = BankAccount("Ryan", "Com Bank", 100)
acc2 = BankAccount("Mich", "HNB", 100000)

print(acc1.get_balance())

acc1.set_balance(-2)
acc1.set_balance(2)

print(acc1.get_balance())