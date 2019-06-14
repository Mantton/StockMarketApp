from yahoo_fin.stock_info import *
from Scripts.orderdetails import Order
import datetime

from Scripts import IO


def get_balance():
    file = open('userinfo.txt', 'r')
    contents = file.readlines()
    first_catch = contents[0].split('=')
    second_catch = float(first_catch[1].rstrip())
    file.close()
    return second_catch


def get_orderCount():
    file = open('userinfo.txt', 'r')
    contents = file.readlines()
    first_catch = contents[1].split('=')
    second_catch = int(first_catch[1].rstrip())
    file.close()
    return second_catch


def write_info():
    file = open('userinfo.txt', "w")
    updated = [f'user_balance = {user_balance}\n', f'order_count = {order_count}']
    file.writelines(updated)
    file.close()


user_balance = get_balance()
currency = '$'
order_count = get_orderCount()
now = datetime.datetime.now()
time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)


def format_time(time):
    output = f'{time[1]}/{time[2]}/{time[0]}'
    return output


while True:
    entry = input('input command : ')
    command = entry.split(', ')
    print(command)
    # if statement for each command
    if command[0] == 'quit':
        print('EXITING TEST ENV 4')
        break
    elif command[0] == 'add':
        try:
            user_balance += int(command[1])
            print(f"New Balance is {currency}{int(user_balance)}")
            write_info()


        except ValueError:
            print('Invalid Input')

    elif command[0] == 'reset':
        user_balance = 100000
        order_count = 0
        print(f'User Balance has been reset to {currency}{user_balance}')
        write_info()
        try:
            IO.clear_orders()
        except:
            print('Please Exit Worksheet')




    elif command[0] == 'show.balance':
        print(f'User Balance is {currency}{user_balance}')
        # To be able to collapse

    elif command[0] == 'buy':
        # this is the hard part
        ticker = command[1].upper()
        amount = int(command[2])
        try:
            print("Processing")
            buy_price = round(get_live_price(ticker), 2)
            amount_due = round(buy_price * amount)

            if amount_due < user_balance:
                print(f'Proceed to buy {amount} shares of {ticker} at ${buy_price} for {currency}{amount_due}?')
                while True:
                    answer = input('[Y/N] : ')
                    if answer == "Y":

                        user_balance -= amount_due

                        order_count += 1
                        newOrder = Order(f'{order_count}', f'{ticker}', buy_price, amount, amount_due,
                                         format_time(time_now))
                        print(f'Order Placed, new Balance is : ${user_balance}\n')
                        print(f'ORDER DETAILS\n\n'
                              f'ORDER ID :{newOrder.order_name}\n'
                              f'ORDER TICKER : {newOrder.ticker}\n'
                              f'TICKER BUY PRICE:{newOrder.buy_price} \n'
                              f'SHARES PURCHASED: {newOrder.stock_amount}\n'
                              f'ORDER VALUE AT PURCHASE:{newOrder.value_atpurchase}\n'
                              f'DATE OF PURCHASE: {format_time(time_now)}')
                        print('')
                        write_info()

                        try:
                            newOrder.save_order()


                        except PermissionError:
                            print('Please Exit the Worksheet')
                            order_count -= 1

                        break

                    elif answer == 'N':
                        print('Order Cancelled')
                        break
                    else:
                        print('INVALID INPUT')

            else:
                print("Insufficient Funds")
                print(f'You require ${amount_due} to buy {amount} stocks of {ticker} ')

        except:
            print('INTERNAL SYSTEM ERROR PLEASE TRY AGAIN')

    elif command[0] == "update.orders":
        IO.update_stocks()
        try:

            IO.update_datasheet()  # FINALLY GOT THIS PIECE OF SHIT TO FUCKING WORK
            # to make it collapse
        except PermissionError:
            print("Please exit the workbook")  # could not mass indent the entire code block
    elif command[0] == 'show.orders':
        print("Processing, This module is in the works...\n\n")
        IO.print_sheets()

    elif command[0] == 'show.portfolio':
        print('Processing, Please note, this module is in the works')
        IO.print_datasheets()
        print('')




    elif command[0] == 'show.help':
        print('COMMANDS: \n'
              'quit : exit program\n'
              'add, value : add a value to your balance\n'
              'reset : reset your balance to $10000\n'
              'show.balance : print out your balance\n'
              'show.help : prints out your help screen\n'
              'show.orders : gives table like veiw of order\n'
              'update.orders: updates database to give realtime values\n'
              'show.portofloi: compiles data of every currently owned stock and give additional info regarding your portfolio')


    else:
        print(" Invalid Syntax, please type 'show.help' to retrieve all documented syntax")
