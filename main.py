# Imports
import argparse
from functions import create_csv_files, report_inventory, buy_item, read_csv_file, print_table, valid_date, update_csv_file, create_date_file, get_date, increase_date, adderFunc
from parser import my_parser
from datetime import date, datetime, timedelta

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

### TO DO
#(•) BUY PRODUCTS
#( ) SELL PRODUCT
#(•) REPORT INVENTORY NOW
#( ) REPORT INVENTORY YESTERDAY
#( ) REPORT REVENUE TODAY
#( ) REPORT REVENUE YESTERDAY
#(•) ADVANCE TIME

# Your code below this line.
def main():
    args = my_parser()

    if args.command == 'buy':
        new_item = [args.product_name, args.price, args.expiration_date]
                
        if None in new_item:
            print('usage: --product-name (str) --price (float) --expiration-date (YYYY/MM/DD: str)')
        elif not valid_date(args.expiration_date):
            print('Incorrect date format, should be YYYY/MM/DD')
        else:
            buy_item(new_item)  
    if args.command == 'sell':
        print("Let's " + args.command)
    if args.command == 'report':
        if args.subcommand == 'inventory':
            if args.now:
                table = read_csv_file('bought.csv')
                print_table(table)
                report_inventory(table['rows'], None, 'today')
            elif args.yesterday:
                pass
            else:
                print('usage: Please specify either now (--now) or yesterday (--yesterday)')    
                
        if args.subcommand == 'revenue':
            if args.today:
                table = read_csv_file('sold.csv')
                print_table(table)
            elif args.yesterday:
                pass
            else:
                print('usage: Please specify either today (--today) or yesterday (--yesterday)')    
    if args.advance_time:
        increase_date(args.advance_time)

if __name__ == "__main__":
    main()
