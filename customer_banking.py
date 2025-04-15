# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("Enter details for the Savings Account:")
    savings_balance = float(input("Enter the initial balance: $"))
    savings_interest_rate = float(input("Enter the interest rate (in percentage): "))
    savings_months = int(input("Enter the number of months: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nSavings Account Results:")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Balance: ${updated_savings_balance:.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print("Enter details for the CD Account:")
    cd_balance = float(input("Enter the initial balance: $"))
    cd_interest_rate = float(input("Enter the interest rate (in percentage): "))
    cd_months = int(input("Enter the number of months: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nCD Account Results:")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated Balance: ${updated_cd_balance:.2f}")


# Ensure that the main function is executed when the script is run directly
if __name__ == "__main__":
    main()
