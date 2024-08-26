atm_users = [
    ["u1", "pw1", 1000],#cus_user,cus_pass,acc_bal
    ["u2", "pw2", 1500],
    ["u3", "pw3", 2000],
    ["u4", "pw4", 500],
    # Add more users as needed
]

cus_user = input("Enter the Username: ").strip().lower()
action = True

for i in atm_users:
    if cus_user == i[0]:
        x = atm_users.index(i)
        amount = atm_users[x][2]
        cus_pass = input("Enter the password?").lower()
        if cus_pass == atm_users[x][1]:
            while action:
                cus_choice = input("Please select from below\n 1 for Deposit\n 2 for Withdraw\n 3 for Balance\n 4 for Exit: ")
                if cus_choice == "1":
                    Deposit = int(input("How much you are planning to deposit?"))
                    amount += Deposit
                    atm_users[x][2] = amount  # Update the balance in the list
                    print("New balance:", amount)
                elif cus_choice == "2":
                    withdraw = int(input("How much you are planning to withdraw?"))
                    if withdraw <= amount:
                        amount -= withdraw
                        atm_users[x][2] = amount  # Update the balance in the list
                        print("New balance:", amount)
                    else:
                        print("Insufficient balance")
                elif cus_choice == "3":
                    print(f"Your balance is {amount}")
                elif cus_choice == "4":
                    action = False
                    print("Thank you for choosing us")
                else:
                    print("Invalid option. Please select again.")
        else:
            print("Wrong Password, Transaction has been canceled!")
        break
else:
    print("Invalid user")

