# winc-superpy
 
The application stores accounts of a shop's purchases and sales. It can calculate the store's inventory, revenue and profit on different moments of time.

The application consists of 3 files: main.py, parser.py and functions.py.

# Main.py
This is the main part of the application that needs to be called to run the program. 
The program first checks if the necessary csv and txt files have been created, otherwise creates them.
Then it calls the parser function to receive the parser commands.

It parses the commands and/or arguments and calls the relevant functions from functions.py with the data provided by the user. 
Also if any arguments or commands are invalid or miss info it alerts the user by printing error messages.

# Functions.py
This file holds all the functions of the program. It gets called from Main.py. Every function has a clear description in the comments.

# Parser.py:
Makes use of the argparse module to handle different commands and arguments.
The structure of the commands is as follows.

### (1) Top-Level:

The Parser takes either the -advance-time argument or one of the following three commands: buy, sell or report.

(a) --advance-time, takes an INT as input and advances the current time (as stored in date.txt) by that amount of days.

(b) buy, takes 3 arguments: name STR, price FLOAT and expiry date STR of the product 

(c) sell, takes 2 arguments: name STR and price FLOAT of the product.

(d) report, takes either on of the following three sub-commands: inventory, revenue or profit.

### (2) Second-Level:

The Report command has it's own sub-parser running the following three commands: inventory, revenue or profit.

(a) inventory, has 3 optional flags, either --now or --yesterday and --export.

(b) revenue, has 3 optional flags, either --today or --yesterday, and one optional argument: a date STR.

(c) profit, has 3 optional flags, either --today or --yesterday, and one optional argument: a date STR.

Parser.py runs the parser as a function that can be called from main.py, and return the parsed arguments.

# CSV and TXT files
The program creates 3 different files in your working directory: bought.csv, sold.csv and date.txt.

### bought.csv
records the bought stock as follows:
id,product_name,buy_date,buy_price,expiration_date

### sold.csv
records the sold stock as follows:
id,product_name,sell_date,sell_price

### date.txt
records the current date as YYYY/MM/DD. This file gets updated whenever the user advances time (--advance-time). This file is called constantly throughout the program to check which entries in bought.csv and sold.csv are relevant.

### COMMANDS
You can run the program with the following commands:
#### $ python3 main.py --advance-time 5
#### $ python3 main.py buy --product-name Kiwi --price 20.0 --expiration-date 2022/02/03
#### $ python3 main.py sell --product-name Kiwi --price 20.0 --expiration-date 2022/02/03
#### $ python3 main.py report inventory --now
#### $ python3 main.py report inventory --yesterday --export
#### $ python3 main.py report profit --yesterday
#### $ python3 main.py report revenue --date 2022/03/07
#### $ python3 main.py report revenue --date 2022/02
