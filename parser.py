import argparse

def my_parser():

    # Create the parser
    parser = argparse.ArgumentParser(description='Main description here')

    # Commands
    subparser = parser.add_subparsers(dest='command')
    
    buy = subparser.add_parser('buy')
    buy.set_defaults(function=buy)
    buy.add_argument('--product-name', type=str, help='Add name of product, in lowercase')
    # buy.add_argument('--count', type=int, help='Add name of product, in lowercase')
    buy.add_argument('--price', type=float, help='Add price of product, as float')
    buy.add_argument('--expiration-date', type=str, help='Add expiration date of product, as yyyy-mm-dd')
    
    sell = subparser.add_parser('sell')
    sell.set_defaults(function=sell)
    
    report = subparser.add_parser('report')
    report.set_defaults(function=report)
    sub_report = report.add_subparsers(dest='subcommand')
    
    revenue = sub_report.add_parser('revenue')
    revenue.add_argument('--today', action="store_true")
    revenue.add_argument('--yesterday', action="store_true")

    inventory = sub_report.add_parser('inventory')
    inventory.add_argument('--now', action="store_true")
    inventory.add_argument('--yesterday', action="store_true")

    # Optional arguments
    parser.add_argument('--advance-time', type=int, help='Advance time by days, as integer')

    # Execute the parse_args() method
    return parser.parse_args()