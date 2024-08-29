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
            else:
                print("Invalid pin.")
        else:
            print("Invalid name.")

main()
