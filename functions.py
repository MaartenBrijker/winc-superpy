import os
import csv
from datetime import date, datetime, timedelta
from tabulate import tabulate

# global paths
CWD = os.getcwd()
BOUGHT = os.path.join(CWD, 'bought.csv')
SOLD = os.path.join(CWD, 'sold.csv')
DATE = os.path.join(CWD, 'date.txt')

# creates bough.csv, sold.csv and date.txt if they don't exist yet
def create_csv_date_files():
    if not os.path.exists(BOUGHT):
        with open(BOUGHT, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id','product_name','buy_date','buy_price','expiration_date'])
    if not os.path.exists(SOLD):
        with open(SOLD, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id','product_name','sell_date','sell_price'])
    if not os.path.exists(DATE):
        with open(DATE, 'w') as f:
            f.write(date.today().strftime("%Y/%m/%d"))

# reads a csv file and returns the header and rows as a dictionary
def read_csv_file(filename):
    rows = []
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return {'header': header, 'rows': rows} 

# uses the tabulate module to print a table
def print_table(table):
    print(tabulate(table['rows'], table['header']))

# reports the inventory for the specified date, either prints it as table or returns it as an object, based on switch
def report_inventory(bought, sold, check_date, switch):
    header = ['product_name','count']
    products_bought = {}
    products_sold = {}
    
    # first get all the type and amounts of products bought
    for row in bought:
        # print(row)
        # if expiry date is not expired and if buy date is not in the future 
        if not is_expired(row[4], check_date) and not date_in_future(row[2], check_date):
            if row[1] in products_bought:
                products_bought[row[1]] += 1
            else:
                products_bought[row[1]] = 1
        
    # then get all the type and amounts of products sold
    for row in sold:
        # if expiry date is not expired and if buy date is not in the future 
        if not date_in_future(row[2], check_date):
            if row[1] in products_sold:
                products_sold[row[1]] += 1
            else:
                products_sold[row[1]] = 1

    # Subtract the sold items from the bought items to get the actual inventory
    inventory = {key: products_bought[key] - products_sold.get(key, 0) for key in products_bought}
    
    if switch == 'return':
        return inventory
    if switch == 'print':        
        # convert numbers values to strings, such that print_table will work
        inventory_as_list = []
        for keys in inventory:
            inventory_as_list.append([keys, str(inventory[keys])])
        print_table({'header': header, 'rows': inventory_as_list})

# reports revenue for the specified date
def report_revenue(sold, check_date):
    revenue = 0.0
    for row in sold:
        if row[2] == check_date:    # only add the sell-price of produc if the sold_date matches
            revenue += float(row[3])
    print(f"{check_date}'s revenue: €{revenue}")

# calculates the amount sold and bought on specified dates, reports back profit
def report_profit(bought, sold, check_date):
    amount_sold = 0.0
    for row in sold:
        if row[2] == check_date:
            amount_sold += float(row[3])
    
    amount_bought = 0.0
    for row in bought:
        if row[2] == check_date:
            amount_bought += float(row[3])
            
    profit = amount_sold - amount_bought
    print(f"{check_date}'s profit: €{profit}")

# checks if the product is expired, returns a boolean
def is_expired(prod_date, check_date):
    expiry_date = datetime.strptime(prod_date, '%Y/%m/%d')
    current_date = datetime.strptime(check_date, '%Y/%m/%d')
    if expiry_date > current_date:
        return False
    return True

# checks if a bought or sold date of product is in the future, returns a boolean
def date_in_future(date, check_date):
    bought_date = datetime.strptime(date, '%Y/%m/%d')
    current_date = datetime.strptime(check_date, '%Y/%m/%d')
    if current_date >= bought_date:
        return False
    return True

# updates the bought or sold csv files with a new table
def update_csv_file(filename, table):
    if os.path.exists(filename):
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(table['header'])
            for row in table['rows']:
                writer.writerow(row)
    else:
        print(f'ERROR: {filename} does not exist')
       
# reads the date.txt file, returns the current date as a string
def get_date():
    with open('date.txt', 'r') as f:
        line = f.readline()
        return line

# increases the date in date.txt with a specified amount
def increase_date(amount):
    current_date = datetime.strptime(get_date(), "%Y/%m/%d")
    new_date = current_date + timedelta(days=amount)
    with open('date.txt', 'w') as f:
        f.write(new_date.strftime("%Y/%m/%d"))

# checks if an expiration date is valid, i.e. is in the future
def valid_expiration_date(date):
    try:
        date_to_check = datetime.strptime(date, '%Y/%m/%d')
        current_date = datetime.strptime(get_date(), '%Y/%m/%d')
        if current_date > date_to_check:
            return False
        return True
    except ValueError:
        return False

# checks if a date has a valid form
def valid_date(date):
    try:
        datetime.strptime(date, '%Y/%m/%d')
        return True
    except ValueError:
        return False

# takes a new_item list containing argparse arguments, adds id and date, updates the original tabel and updates bought.csv    
def buy_item(new_item):
    date = get_date()
    table = read_csv_file('bought.csv')
    id = len(table['rows'])
    new_item.insert(0, id)
    new_item.insert(2, date)
    table['rows'].append(new_item)
    update_csv_file('bought.csv', table)
    print('OK')
    
# takes a new_item list containing argparse arguments, checks whether item is in stock, updates sold.csv
def sell_item(new_item):
    date = get_date()
    sold = read_csv_file('sold.csv')
    bought= read_csv_file('bought.csv')
    inventory = report_inventory(bought['rows'], sold['rows'], date, 'return')
    
    # based on the inventory check if product exists and whether there is sufficient stock    
    if new_item[0] not in inventory or inventory[new_item[0]] <= 0:
        print(f"Unsufficient stock of {new_item[0]}'s. Unable to sell.")
    else: # add item to sold.csv
        id = len(sold['rows'])
        new_item.insert(0, id)
        new_item.insert(2, date)
        sold['rows'].append(new_item)
        update_csv_file('sold.csv', sold)            
        print('OK')         