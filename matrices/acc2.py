class AccountMatrix:
    def __init__(self, num_accounts, num_months):
        self.num_accounts = num_accounts
        self.num_months = num_months
        self.matrix = [[0] * num_months for _ in range(num_accounts)]

    def update_balance(self, account_id, month, balance):
        if 0 <= account_id < self.num_accounts and 0 <= month < self.num_months:
            self.matrix[account_id][month] = balance
        else:
            print("Invalid account or month")

    def total_balance(self, account_id):
        if 0 <= account_id < self.num_accounts:
            return sum(self.matrix[account_id])
        else:
            print("Invalid account")
            return 0

    def average_balance(self, month):
        if 0 <= month < self.num_months:
            total = sum(
                self.matrix[account][month] for account in range(self.num_accounts)
            )
            return total / self.num_accounts
        else:
            print("Invalid month")
            return 0

    def total_balance_by_month(self, month):
        if 0 <= month < self.num_months:
            return sum(
                self.matrix[account][month] for account in range(self.num_accounts)
            )
        else:
            print("Invalid month")
            return 0


# Example usage:

account_matrix = AccountMatrix(3, 12)  # Create a matrix with 3 accounts and 12 months

account_matrix.update_balance(0, 5, 1000)  # Update the balance of account 0 for month 5
account_matrix.update_balance(1, 5, 1500)  # Update the balance of account 1 for month 5
account_matrix.update_balance(2, 5, 2000)  # Update the balance of account 2 for month 5

print("Total balance of account 1:", account_matrix.total_balance(1))

print("Average balance for month 5:", account_matrix.average_balance(5))

print(
    "Total balance for all accounts in month 5:",
    account_matrix.total_balance_by_month(5),
)
