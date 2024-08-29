def main():
    pinCode = ["1111", "2222", "3333", "4444", "5555"] # Data of the account holders
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

                print("\n\nThank you for using this MINI ATM System. \n  !Brought To You By Chaithanya raj Bulla!")
            else:
                print("Invalid pin.")
        else:
            print("Invalid name.")

main()
