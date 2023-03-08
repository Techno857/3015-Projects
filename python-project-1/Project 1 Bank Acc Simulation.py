account_name = input('Please enter the name of your account: ')
initial_balance = float(input('Please enter the starting balance: '))

total_balance = 0.0 + round(initial_balance, 2)
times_deposited = 0
overall_deposits = 0.0
overall_withdrawals = 0.0
successful_withdrawals = 0
unsuccessful_withdrawals = 0
total_amount_failed_to_be_withdrawn = 0.0
penalties = 0.0

print('Account: ', account_name)
print('Balance: ', '$' + str(initial_balance))
print('')
option = 0

while option == 0:
    print('1) Deposit some funds')
    print('2) Withdraw some funds')
    print('3) Quit')
    print('')
    option = int(input('What number option will it be?: '))
    print('')
    if option == 1:
        dep_confirmation = str.lower(input('Do you wish to deposit funds to your account?: '))
        print('')
        if dep_confirmation == 'no':
            print('Exiting to menu...')
            print('')
            option = option - option 
        while dep_confirmation == 'yes':
            deposit = float(input("Please input deposit amount (If you wish to exit this menu, input '0' in the window): "))
            deposit = round(deposit, 2)
            if deposit == 0.0:
                dep_confirmation = 'no'
                print('Exiting to menu...')
                print('')
                option = option - option
            elif deposit < 0:
                print('Please input a non-negative value')
                print('')
            else: 
                total_balance += deposit
                overall_deposits += deposit
                times_deposited += 1
                print('')
                print('Account: ', account_name)
                print('Deposit successful, current balance: $' + str(round(total_balance, 2)))
                print('')
    if option == 2:
        withd_confirmation = str.lower(input('Do you wish to withdraw funds from your account?: '))
        print('')
        if withd_confirmation == 'no':
            print('Exiting to menu...')
            print('')
            option = option - option 
        while withd_confirmation == 'yes':
            amount_to_withdraw = float(input("Please input withdrawal amount (If you wish to exit this menu, input '0' in the window): "))
            amount_to_withdraw = round(amount_to_withdraw, 2)
            if amount_to_withdraw == 0:
                withd_confirmation = 'no'
                print('Exiting to menu...')
                print('')
                option = option - option
            elif amount_to_withdraw < 0:
                print('Please input a non-negative value')
                print('')
                unsuccessful_withdrawals += 1
            elif amount_to_withdraw > total_balance:
                total_balance = round(total_balance, 2) - 5.0
                unsuccessful_withdrawals += 1
                penalties += 5.0
                amount_failed_to_be_withdrawn = round(amount_to_withdraw, 2)
                total_amount_failed_to_be_withdrawn += round(amount_failed_to_be_withdrawn, 2)
                print('')
                print('Account: ', account_name)
                print('')
                print('It appears you do not have the required funds needed to complete this withdrawal. Due to this inconvenience, we have take the liberty of charging your account with an overdraft fee of $5.00.')
                print('')
                print('Amount failed to be withdrawn: $' + str(round(amount_failed_to_be_withdrawn, 2)))
                option = option - option 
            elif amount_to_withdraw <= total_balance:
                successful_withdrawals += 1
                total_balance -= amount_to_withdraw
                overall_withdrawals += amount_to_withdraw
                print('Account: ', account_name)
                print('')
                print('Withdrawal was completed successfully, your new balance is: $' + str(round(total_balance, 2)))
    if option == 3:
        print('Final Account Statement')
        print('')
        print('Account: ', account_name)
        print('')
        print('Deposits:')
        print('')
        print('Final account balance : $' + str(round(total_balance, 2)))
        print('Total amount of times deposited (Not including starting balance): ' + str(times_deposited))
        print('Total amount of overall deposits (Not including starting balance): $' + str(round(overall_deposits, 2)))
        print('')
        print('Withdrawals:')
        print('')
        print('Overall amount withdrawn: $' + str(round(overall_withdrawals, 2)))
        print('Successful withdrawals: ' + str(successful_withdrawals))
        print('Unsuccessful withdrawals: ' + str(unsuccessful_withdrawals))
        print('Amount that failed to be withdrawn: $' + str(round(total_amount_failed_to_be_withdrawn, 2)))
        print('Total penalty amount charged: $' + str(round(penalties, 2)))
        print('')
        print("You've reached the end of the program; thankyou for choosing our banking services. If you happened to encounter any bugs or errors in our system, dont hesitate to contact our developer team. Even thought they most likely wont answer back, we'd still love to hear from our beloved users. We hope you enjoyed your experience, have a lovely day!")
