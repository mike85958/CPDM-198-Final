# --------------------------------------------------------
# Michael Rivera
# Final Project
# 4/25/2021
# Banking Project
# ---------------------------------------------------------

 
# _________________________________________________________________________________________
# Customer Class takes in Customer Name and SSN .
# __________________________________________________________________________________________
class Customer:
    
    def __init__(self, strFirstName, strLastName, intSocialSecurityNumber):
        """
        Constructor class to instantiate a customer.
        """
        self.strFirstName = strFirstName
        self.strLastName = strLastName 
        self.intSocialSecurityNumber = intSocialSecurityNumber 

    #getter for property firstname
    @property
    def strFirstName(self):
        return self.__strFirstName

    #setter for firstName
    @strFirstName.setter
    def strFirstName(self, strFirstName):
        try:
            strFirstName = str(strFirstName)
            self.__strFirstName = strFirstName
        except ValueError:
            strFirstName = int(0)
            raise Exception("Input Must be String.")

    #getter for property Last Name
    @property
    def strLastName(self):
        return self.__strLastName

    #setter for Last Name
    @strLastName.setter
    def strLastName(self, strLastName):
        try:
            strLastName = str(strLastName)
            self.__strLastName = strLastName
        except ValueError:
            strLastName = int(0)
            raise Exception("Input Must be String.")

    #getter for SSN
    @property
    def intSocialSecurityNumber(self):
        return self.__intSocialSecurityNumber

    #setter for SSN
    @intSocialSecurityNumber.setter
    def intSocialSecurityNumber(self, intSocialSecurityNumber):
        try:
            intSocialSecurityNumber = int(intSocialSecurityNumber)
            if(len(str(intSocialSecurityNumber)) == 9):
                self.__intSocialSecurityNumber = intSocialSecurityNumber
            else:
                raise Exception("Social Security Numbers must be 9 digits long.")
        except ValueError:
            intSocialSecurityNumber = int(0)
            raise Exception("Input Must be Numeric only.")

# _________________________________________________________________________________________
# Class Account takes in Account Type and Balance then
# uses methods to either Deposit or Withdrawl from Accounts.
# __________________________________________________________________________________________

class Account():

    def __init__(self, strAccountType, dblBalance):
        self.strAccountType = strAccountType
        self.dblBalance = dblBalance

    #getter for property AccountType
    @property
    def strAccountType(self):
        return self.__strAccountType

    #setter for Account Type
    @strAccountType.setter
    def strAccountType(self, strAccountType):
        try:
            strAccountType = str(strAccountType)
            if strAccountType == 'C' or strAccountType == 'S':
                self.__strAccountType = strAccountType
                return 
            else:
                raise Exception("Account Input Must be (C)hecking or (S)avings.")
        except ValueError:
            strAccountType = int(0)
            raise Exception("Input Must be String Checking or Savings.")

    #getter for Balance 
    @property
    def dblBalance(self):
        return self.__dblBalance

    #setter for Balance
    @dblBalance.setter
    def dblBalance(self, dblBalance):
        try:
            dblBalance = float(dblBalance)
            self.__dblBalance = dblBalance
        except ValueError:
            dblBalance = str()
            raise Exception("Balance Input must be Numeric only.")

# Deposit Balance Method
    def deposit_checking(self, dblBalance):

        # Validate Balance first
        try:
            dblBalance = float(dblBalance)
            if dblBalance > 0:
                self.dblBalance += dblBalance
                dblCheckingDeposit = dblBalance
                return dblCheckingDeposit
            else:
                print("Deposit must be greater than 0.")
        except ValueError:
                dblBalance = str()
                print("Invalid input. Must be a Cash Value.")

# Deposit to Savings Account
    def deposit_savings(self, dblBalance):

        try:
            dblBalance = float(dblBalance)
            if dblBalance > 0:
                self.dblBalance = dblBalance
                dblSavingsDeposit += dblBalance
                if dblSavingsDeposit < 500:
                    dblSavingsDeposit -= dblBalance
                    print("The minimum deposit for a Saving Account is $500.")
                return dblSavingsDeposit
            else:
                print("Deposit must be greater than 0.")
        except ValueError:
                dblBalance = str()
                print("Invalid input. Must be a Cash Value.")

# Withdrawl to Checking Account
    def whithdrawl_checking(self, dblBalance):

        try:
            dblBalance = float(dblBalance)
            if dblBalance > 0:
                self.dblBalance = dblBalance
                dblWithdrawChecking -= dblBalance
                if dblWithdrawChecking < 0:
                    dblWithdrawChecking = dblWithdrawSavings - 20
                    print("Your Checking account will be charged a $20 fee.")

                return dblWithdrawChecking
            else:
                print("Withdrawl must be greater than 0.")
        except ValueError:
                dblBalance = str()
                print("Invalid input. Must be a Cash Value.")

# Withdrawl to Savings Account
    def withdrawl_savings(self, dblBalance):

        try:
            dblBalance = float(dblBalance)
            if dblBalance > 0:
                self.dblBalance = dblBalance
                dblWithdrawSavings -= dblBalance
                if dblWithdrawSavings < 500:
                    dblWithdrawSavings += dblBalance
                    print("Savings Account balance cannot go below minimum $500. ")
                return dblWithdrawSavings
            else:
                print("Withdrawl must be greater than 0.")
        except ValueError:
                dblBalance = str()
                print("Invalid input. Must be a Cash Value.")



#class Account(Customer):

#    def __init__(self, strFirstName, strLastName, intSocialSecurityNumber):
#        Customer.__init__(self, strFirstName, strLastName, intSocialSecurityNumber)
#        self.strAccountType = 0
#        self.dblCheckingBalance = 0
#        self.dblSavingsBalance = 0

    #def AccountType(self):
    #    strAccountType = input("What (C)hecking or (S)avings account?: ")
    #    try:
    #            strAccountType = str(strAccountType)
    #            if strAccountType == 'C' or strAccountType == 'S':
    #                self.__strAccountType = strAccountType
    #                return strAccountType
    #            else:
    #                raise Exception("Account Input Must be (C)hecking or (S)avings.")
    #    except ValueError:
    #            strAccountType = int(0)
    #            raise Exception("Input Must be String (C)hecking or (S)avings.")

            

# _________________________________________________________________________________________
# Balance Class takes inherits Customer and Account and 
# uses methods to either Display Balances.
# __________________________________________________________________________________________


class Balances(Customer, Account):

    def __init__(self, strFirstName, strLastName, intSocialSecurityNumber, strAccountType, dblBalance):
        Customer.__init__(self, strFirstName, strLastName, intSocialSecurityNumber)
        Account.__init__(self, strAccountType, dblBalance )

    def __str__(self):
        return Customer.__str__


    def Display_Balances(self):

        print("Customer ", self.strFirstName, " ", self.strLastName, " Balances: ", "Checking:", 
              "${:,.2f}".format(dblCheckingDeposit), 
              "Savings:", "${:,.2f}".format(dblSavingsDeposit))


#def Main():
#tested creating selectable menu options 


 #   while True:
 #       print("""
 #       Bank Account Selections
 #       1. Open New Account for Customer
 #       2. Erase Account from Customer
 #       3. Deposit to Account
 #       4. Withdrawl from Account
 #       5. Show Balances
 #       """)
        
# ----------------------Test Logic---------------------------

# Create multiple customer accounts
Customer1 = Customer("Marky", "Mark", 555227777)
Customer2 = Customer("Mike", "Rivera", 655223333)
Customer3 = Customer("Sally", "May", 123456789)
Customer4 = Customer("Bill", "Gates", 987654321)

# Existing Account Standing
Customer1 = Account("S", 50)
Customer1 = Account("C", 25)
Customer2 = Account("C", 5)


# Deposits into Accounts
Deposit1 = Customer1.deposit_checking(7)
Deposit2 = Customer1.deposit_savings(8)

# Withdrawl from Accounts
Withdrawl1 = Customer1.whithdrawl_checking(20)


# Display Balances
print(Customer1.__str__)
print(Customer1.dblBalance)
print(Customer2.dblBalance)
print(Deposit1)

