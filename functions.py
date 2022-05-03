import os
import csv
from datetime import date, datetime, timedelta

def create_csv_files():
    cwd = os.getcwd()
    # Create bought.csv if it doesn't exist yet.
    if not os.path.exists(cwd+'/bought.csv'):
        with open(cwd+'/bought.csv', 'wb') as f:
            writer = csv.writer(f)
            description_row = ['id','product_name','buy_date','buy_price','expiration_date']
            writer.writerow(description_row)
    # Create sold.csv if it doesn't exist yet.
    if not os.path.exists(cwd+'/sold.csv'):
        with open(cwd+'/sold.csv', 'wb') as f:
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
    print(header)
    print(rows)     
    
def append_csv_file(filename, item):
    pass
       
def create_date_file():
    cwd = os.getcwd()
    path = cwd + '/date.txt'
    # Create bought.csv if it doesn't exist yet.
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(date.today().strftime("%Y/%m/%d"))
            
def read_date():
    # cwd = os.getcwd()
    with open('date.txt', 'r') as f:
        line = f.readline()
        print(line)
        return line

def increase_date(amount):
    current_date = datetime.strptime(read_date(), "%Y/%m/%d")
    delta =  timedelta(days=amount)
    new_date = current_date + timedelta(days=amount)
    print('newdate: ', new_date)
    with open('date.txt', 'wb') as f:
        f.write(date.today().strftime("%Y/%m/%d"))
    
def adderFunc(n1, n2):
    return n1 + n2
