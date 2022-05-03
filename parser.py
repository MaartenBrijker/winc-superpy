import argparse

def my_parser():

    # Create the parser
    parser = argparse.ArgumentParser(description='Add two chosen numbers')

    # Commands
    subparser = parser.add_subparsers(dest='command')
    buy = subparser.add_parser('buy')
    buy.set_defaults(function=buy)
    sell = subparser.add_parser('sell')
    sell.set_defaults(function=sell)
    report = subparser.add_parser('report')
    report.set_defaults(function=report)

    # Optional arguments
    parser.add_argument('--action', type=str, help='Add action, mandatory, either buy, sell, report')
    parser.add_argument('--product-name', type=str, help='Add name of product, in lowercase')
    parser.add_argument('--price', type=float, help='Add price of product, as float')
    parser.add_argument('--expiration-date', type=str, help='Add expiration date of product, as yyyy-mm-dd')
    parser.add_argument('--advance-time', type=int, help='Advance time by days, as integer')

    # Execute the parse_args() method
    return parser.parse_args()