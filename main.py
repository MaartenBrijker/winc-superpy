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
    
    create_csv_files()
    create_date_file()
    read_date()
    read_csv_file('bought.csv')
    read_csv_file('sold.csv')
    # print(adderFunc(args.number1, args.number2))
    if args.command == 'buy':
        print("Let's " + args.command)
    if args.command == 'sell':
        print("Let's " + args.command)
    if args.command == 'report':
        print("Let's " + args.command)
    # if args.advance_time:
        # increase_date(args.advance_time)
        # read_date()


if __name__ == "__main__":
    main()
