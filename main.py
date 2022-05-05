# Imports
import argparse
from functions import create_csv_date_files, report_profit, valid_date, report_revenue, sell_item, report_inventory, buy_item, read_csv_file, print_table, valid_expiration_date, update_csv_file, get_date, increase_date
from parser import my_parser
from datetime import date, datetime, timedelta

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

### COMMANDS
# python3 main.py report inventory --now
# python3 main.py buy --product-name Kiwi --price 20.0 --expiration-date 2022/02/03

def main():
    # request the parser from parser.py
    args = my_parser()

    # runs everytime to check if the bought, sold and date files exist or have to be made
    create_csv_date_files()
    
    if args.command == 'buy':
        # creates a list with the arguments, then checks whether all of them are provided
        new_item = [args.product_name, args.price, args.expiration_date]  
        if None in new_item:
            print('usage: --product-name (str) --price (float) --expiration-date (YYYY/MM/DD: str)')
        elif not valid_expiration_date(args.expiration_date):
            print('Incorrect date format, should be YYYY/MM/DD, and expiration date should be in the future.')
        else:
            buy_item(new_item)  

    if args.command == 'sell':
        # creates a list with the arguments, then checks whether all of them are provided
        new_item = [args.product_name, args.price]
        if None in new_item:
            print('usage: --product-name (str) --price (float)')
        else:
            sell_item(new_item)     
             
    if args.command == 'report':
        if args.subcommand == 'inventory':
            if not args.yesterday and not args.now:
                print('usage: Please specify either now (--now) or yesterday (--yesterday)')  
            else:
                use_date = get_date()
                if args.yesterday:  # if inventory is requested for yesterday, adjust date for report_inventory() 
                    current_date = datetime.strptime(get_date(), "%Y/%m/%d")
                    use_date = (current_date + timedelta(days=-1)).strftime("%Y/%m/%d")
                bought = read_csv_file('bought.csv')
                sold = read_csv_file('sold.csv')
                report_inventory(bought['rows'], sold['rows'], use_date, 'print')
    
        # setting the relevant date is similar for both profit and revenue commands
        if args.subcommand == 'revenue' or args.subcommand == 'profit':
            if not args.yesterday and not args.today and not args.date:
                print('usage: Please specify either today (--today) or yesterday (--yesterday)')    
            else:
                use_date = get_date()
                if args.yesterday:  # if revenue is requested for yesterday, adjust date for report_inventory() 
                    current_date = datetime.strptime(get_date(), "%Y/%m/%d")
                    use_date = (current_date + timedelta(days=-1)).strftime("%Y/%m/%d")
                elif args.date:
                    if valid_date(args.date):
                        use_date = args.date
                    else:
                        print('Incorrect date format, should be YYYY/MM/DD')
                # after the date's set we run the relevant functions based on the command
                sold = read_csv_file('sold.csv')
                if args.subcommand == 'revenue':
                    report_revenue(sold['rows'], use_date) 
                if args.subcommand == 'profit':       
                    bought = read_csv_file('bought.csv')
                    report_profit(bought['rows'], sold['rows'], use_date) 
                    
    if args.advance_time:
        increase_date(args.advance_time)

if __name__ == "__main__":
    main()
