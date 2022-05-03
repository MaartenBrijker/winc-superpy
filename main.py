# Imports
import argparse
from functions import create_csv_files, read_csv_file, append_csv_file, create_date_file, read_date, increase_date, adderFunc
from parser import my_parser

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.
def main():
    
    args = my_parser()
    
    # create_csv_files()
    # create_date_file()
    read_date()
    # read_csv_file('bought.csv')
    # read_csv_file('sold.csv')
    # print(adderFunc(args.number1, args.number2))
    if args.command == 'buy':
        print("Let's " + args.command)
    if args.command == 'sell':
        print("Let's " + args.command)
    if args.command == 'report':
        print("Let's " + args.command)
    if args.advance_time:
        increase_date(args.advance_time)
        read_date()

# # Create the parser
# parser = argparse.ArgumentParser(description='Add two chosen numbers')

# # Commands
# subparser = parser.add_subparsers(dest='command')
# buy = subparser.add_parser('buy')
# buy.set_defaults(function=buy)
# sell = subparser.add_parser('sell')
# sell.set_defaults(function=sell)
# report = subparser.add_parser('report')
# report.set_defaults(function=report)

# # Optional arguments
# parser.add_argument('--action', type=str, help='Add action, mandatory, either buy, sell, report')
# parser.add_argument('--product-name', type=str, help='Add name of product, in lowercase')
# parser.add_argument('--price', type=float, help='Add price of product, as float')
# parser.add_argument('--expiration-date', type=str, help='Add expiration date of product, as yyyy-mm-dd')
# parser.add_argument('--advance-time', type=int, help='Advance time by days, as integer')

# # Execute the parse_args() method
# args = parser.parse_args()

if __name__ == "__main__":
    main()
