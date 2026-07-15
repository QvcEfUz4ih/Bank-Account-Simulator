print("================================")
print(" Bank Accouunt Simulator ")
print("================================")


account_name = input("Enter account holder's name: ")

current_balance =float(input("Enter current balance: "))
deposit_amount = float(input("Enter deposit amount: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))


new_balance = current_balance + deposit_amount - withdrawal_amount

if new_balance < 0:
    status = "Account overdrawn"
    

elif new_balance < 500:
    status = "Low Balance"


else:
    status = "Account is Healthy"
    

print()
print("Account Summary")
print("===============================")
print("Account Holder:", account_name)
print("Current Balance:R", current_balance)
print("Deposit: R", deposit_amount)
print("Withdrawal: R", withdrawal_amount)
print("New Balance: R", new_balance)
print("Status:", status)


















