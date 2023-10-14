import csv


class AccountMatrix:
    def __init__(self, num_accounts, num_months):
        # Initialize the accounnit matrix with all balances set to 0.
        self.matrix = [[0 for _ in range(num_months)] for _ in range(num_accounts)]

    def update_balance(self, account_id, month, balance):
        # Update the balance of the account with the specified account_id for the specified month.
        self.matrix[account_id][month] = balance

    def total_balance(self, account_id):
        # Returns the total balance of the account with the specified account_id.
        total_balance = 0
        for month in range(len(self.matrix[0])):
            total_balance += self.matrix[account_id][month]
        return total_balance

    def average_balance(self, month):
        # Returns the average balance across all accounts for the specified month.
        total_balance = 0
        for account_id in range(len(self.matrix)):
            total_balance += self.matrix[account_id][month]
        return total_balance / len(self.matrix)

    def total_balance_by_month(self, month):
        # Returns the total balance for all accounts in the specified month.
        total_balance = 0
        for account_id in range(len(self.matrix)):
            total_balance += self.matrix[account_id][month]
        return total_balance

    def save_to_file(self, filename):
        # Save the account matrix to a file.
        with open(filename, "w") as f:
            for row in self.matrix:
                f.write(",".join([str(balance) for balance in row]) + "\n")

    def load_from_file(self, filename):
        # Load the account matrix from a file.
        with open(filename, "r") as f:
            for row in f.readlines():
                self.matrix.append([float(balance) for balance in row.split(",")])


# Example usage:

matrix = AccountMatrix(3, 6)
matrix.update_balance(0, 2, 1000)
matrix.update_balance(1, 2, 1500)
matrix.update_balance(2, 2, 2000)

print(matrix.total_balance(1))  # Should print 1500
print(matrix.average_balance(2))  # Should print 1000
print(matrix.total_balance_by_month(2))  # Should print 4500

# Save the account matrix to a file.
matrix.save_to_file("account_matrix.csv")

# Load the account matrix from a file.
matrix = AccountMatrix(1, 1)
matrix.load_from_file("account_matrix.csv")

# Print the total balance of the account.
print(matrix.total_balance(0))  # Should print 4500
