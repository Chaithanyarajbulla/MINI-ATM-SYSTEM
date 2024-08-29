# MINI ATM System

## Introduction
The **MINI ATM System** is a simple Python program designed to simulate a basic ATM machine. It allows users to check their account details, withdraw money, and deposit money. This project is ideal for beginners who want to understand the basics of Python, loops, conditionals, and list handling.

## Features
- **Account Authentication:** Users can authenticate themselves using their name and a PIN code.
- **Account Details:** Displays the account number and balance of the authenticated user.
- **Withdraw Funds:** Users can withdraw money from their account. The system checks if the withdrawal amount is less than or equal to the current balance.
- **Deposit Funds:** Users can deposit money into their account, which updates the balance accordingly.

## How It Works
1. **Authentication:** 
   - Users are prompted to enter their name and PIN.
   - The system checks if the entered name and PIN match any account in the database.
   
2. **Account Details:**
   - If the authentication is successful, the user's account number and balance are displayed.
   
3. **Withdraw or Deposit:**
   - Users can choose to withdraw or deposit money.
   - The system updates the balance accordingly and displays the new balance.

4. **Invalid Data Handling:**
   - If an incorrect name or PIN is entered, the system will prompt the user to try again.

## Code

```python
def main():
    pinCode = ["1111", "2222", "3333", "4444", "5555"]  # Data of the account holders
    accountHoldersName = ["niroop", "bablu", "kanna", "rinky", "chaithanya"]
    accountNumber = ['1353', '199281', "182838", "185597", "667432"]
    balance = [1000000, 2000000, 3000000, 4000000, 5000000]

    for i in range(0, 999999999):  # Infinite loop
        print("""
    \t\t=== Welcome To MINI ATM System ===
""")
        inputName = input("Enter Your Name: ").lower()

        if inputName in accountHoldersName:
            index = accountHoldersName.index(inputName)  # Get the index of the account holder's name
            inputPin = input("\nEnter Pin Number: ")

            if inputPin == pinCode[index]:
                print("\nYour account number is: ", accountNumber[index])
                print("Your account balance is: Rs.", balance[index])
                drawOrDeposite = input("\nDo you want to draw or deposit cash (draw/deposit/no): ")

                if drawOrDeposite == "draw":
                    amount = input("\nEnter the amount you want to draw: ")
                    try:
                        amount = int(amount)
                        if amount > balance[index]:
                            raise ValueError("Insufficient balance.")
                    except ValueError as e:
                        print(e)
                        continue
                    remainingBalance = balance[index] - amount
                    balance[index] = remainingBalance
                    print("\nYour available balance is: ", remainingBalance)

                elif drawOrDeposite == "deposit":
                    amount = input("Enter the amount you want to deposit: ")
                    try:
                        amount = int(amount)
                    except ValueError:
                        print("Invalid amount.")
                        continue
                    remainingBalance = balance[index] + amount
                    balance[index] = remainingBalance
                    print("Your available balance is: ", remainingBalance)

                print("\n\nThank you for using this Simple ATM System. \n  Brought To You By Chaithanya raj Bulla")
            else:
                print("Invalid pin.")
        else:
            print("Invalid name.")

main()
