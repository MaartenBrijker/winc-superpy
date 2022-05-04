import os
import csv
from datetime import date, datetime, timedelta
from tabulate import tabulate

def create_csv_files():
    cwd = os.getcwd()
    # Create bought.csv if it doesn't exist yet.
    if not os.path.exists(cwd+'/bought.csv'):
        with open(cwd+'/bought.csv', 'w') as f:
            writer = csv.writer(f)
            description_row = ['id','product_name','buy_date','buy_price','expiration_date']
            writer.writerow(description_row)
    # Create sold.csv if it doesn't exist yet.
    if not os.path.exists(cwd+'/sold.csv'):
        with open(cwd+'/sold.csv', 'w') as f:
            writer = csv.writer(f)
            description_row = ['id','bought_id','sell_date','sell_price']
            writer.writerow(description_row)

def read_csv_file(filename):
    rows = []
    with open(filename, 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return {'header': header, 'rows': rows} 

def print_table(table):
    print(table)
    print(tabulate(table['rows'], table['header']))

def report_inventory(bought, sold, inventory_date):
    products_bought = {}    # empty dictionary, add product name: [amount] # only add products up to date and that are not expired
    products_sold = {}
    header = ['product_name','count']

    # first get all the type of products bought
    for row in bought:
        if row[1] in products_bought:
            products_bought[row[1]] += 1
        else:
            products_bought[row[1]] = 1
            
    # convert numbers values to strings, such that print_table will work
    products_as_list = []
    for keys in products_bought:
        products_as_list.append([keys, str(products_bought[keys])])
    
    print(products_as_list)
    print_table({'header': header, 'rows': products_as_list})
    
def update_csv_file(filename, table):
    cwd = os.getcwd()
    path = cwd+filename
    print(path)
    if os.path.exists(filename):
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            # description_row = ['id','product_name','buy_date','buy_price','expiration_date']
            # writer.writerow(description_row)
            writer.writerow(table['header'])
            for row in table['rows']:
                writer.writerow(row)
    else:
        print('ERROR: bought.csv does not exist')
       
def create_date_file():
    cwd = os.getcwd()
    path = cwd + '/date.txt'
    # Create bought.csv if it doesn't exist yet.
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(date.today().strftime("%Y/%m/%d"))
            
def get_date():
    # cwd = os.getcwd()
    with open('date.txt', 'r') as f:
        line = f.readline()
        return line

def increase_date(amount):
    current_date = datetime.strptime(get_date(), "%Y/%m/%d")
    new_date = current_date + timedelta(days=amount)
    with open('date.txt', 'w') as f:
        f.write(new_date.strftime("%Y/%m/%d"))
    
def adderFunc(n1, n2):
    return n1 + n2

def valid_date(date):
    try:
        datetime.strptime(date, '%Y/%m/%d')
        return True
    except ValueError:
        return False

def buy_item(new_item):
    date = get_date()
    table = read_csv_file('bought.csv')
    id = len(table['rows'])
    new_item.insert(0, id)
    new_item.insert(2, date)
    table['rows'].append(new_item)
    update_csv_file('bought.csv', table)
    print_table(read_csv_file('bought.csv'))
    print('OK')         