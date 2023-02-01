import random
import logging
import sys
from datetime import datetime

#def logger from class logging
logger = logging.getLogger(__name__)
#set level report
logger.setLevel(logging.INFO)

streanhandler =logging.StreamHandler(sys.stdout)
filehandler2 = logging.FileHandler("my_files.log")

formatter_form = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_form2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

streanhandler.setFormatter(formatter_form)
filehandler2.setFormatter(formatter_form2)

logger.addHandler(streanhandler)
logger.addHandler(filehandler2)


#1simple mod
logging.basicConfig(filename="ATM_RECORDS.log", level=logging.INFO, format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s'")



class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    
  def authenticate(self):
    count =0
    while True:

      pin = int(input("Enter account pin: "))
      print(count)
      if pin != 1234:
        
        logger.log(logging.INFO, "Error! Invalid pin. Try again.")
        count +=1
        if count > 2:
            logging.warning("Too many attempts, card locked")
           # print("Too many attempts, card locked")    
            quit()            
      else:
        return None
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      if amount < 0:
        logger.warning("Warning! You entered a negative number to deposit.")
      self.balance += amount
      logger.info("Amount Deposited: ${amount}".format(amount=amount))
      logger.info("Transaction Info:  ")
      logger.info("Status: Successful")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
    except ValueError:
      logger.error("Error! You entered a non-number value to deposit.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        logger.info("You withdrew: ${amount}".format( amount=amount))
        logger.info("Transaction Info:")
        logger.info("Status: Successful")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        logger.error("Error! Insufficient balance to complete withdraw.")
        logger.info("Transaction Info:")
        logger.info("Status: Failed")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.error("Error! You entered a non-number value to withdraw.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def display(self):
    print("Available Balance = ${balance}".format(balance=self.balance))
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()