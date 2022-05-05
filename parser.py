import argparse

def my_parser():
    
    # Create the Main Parser
    parser = argparse.ArgumentParser(description='Main description here')
    
    # The Parser has one optional argument, to advance time with a certain amount of days
    parser.add_argument('--advance-time', type=int, help='Advance time by days, as integer')

    # We create a Subparser on the Main Parser for the Buy, Sell and Report commands.
    subparser = parser.add_subparsers(dest='command')
    
    # The Buy parser takes 3 arguments: Name, Price and Exp. Date of product.
    buy = subparser.add_parser('buy')
    buy.set_defaults(function=buy)
    buy.add_argument('--product-name', type=str, help='Add name of product, as str')
    buy.add_argument('--price', type=float, help='Add price of product, as float')
    buy.add_argument('--expiration-date', type=str, help='Add expiration date of product, as yyyy-mm-dd')
    
    # The Sell parser takes 3 arguments: Name and Price of product.
    sell = subparser.add_parser('sell')
    sell.set_defaults(function=sell)
    sell.add_argument('--product-name', type=str, help='Add name of product, in lowercase')
    sell.add_argument('--price', type=float, help='Add price of product, as float')

    # The Report parser has it's own Sub Parser (sub_report) to handle the Revenue, Inventory and Profit commands.
    report = subparser.add_parser('report')
    report.set_defaults(function=report)
    sub_report = report.add_subparsers(dest='subcommand')
    
    # The Revenue parser has 2 optional flags, either today or yesterday, and one optional argument: a date.
    revenue = sub_report.add_parser('revenue')
    revenue.add_argument('--today', action="store_true", help='Add the --today flag to get the revenue of today')
    revenue.add_argument('--yesterday', action="store_true", help='Add the --yesterday flag to get the revenue of yesterday')
    revenue.add_argument('--date', type=str, help='Add --date and a valid date (YYYY/MM/DD) to receive the revenue of that date')

    # The Inventory parser has 2 optional flags, either now or yesterday.
    inventory = sub_report.add_parser('inventory')
    inventory.add_argument('--now', action="store_true", help='Add the --now flag to get the inventory of today')
    inventory.add_argument('--yesterday', action="store_true", help='Add the --yesterday flag to get the inventory of yesterday')
    
    # The Profit parser has 2 optional flags, either today or yesterday, and one optional argument: a date.
    profit = sub_report.add_parser('profit')
    profit.add_argument('--today', action="store_true",  help='Add the --today flag to get the profit of today')
    profit.add_argument('--yesterday', action="store_true", help='Add the --yesterday flag to get the profit of yesterday')
    profit.add_argument('--date', type=str, help='Add --date and a valid date (YYYY/MM/DD) to receive the profit of that date')

    # Execute the parse_args() method and return it
    return parser.parse_args()