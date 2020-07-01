from time import sleep

#our class  Parent
class DemirBank:
    __balance = 0 #private data
    __id = 0    #private data
    _personal_info = {}  #protected data
    
    #Magic function
    def  __init__(self, name, surname, amount, id, pin): 
        self._personal_info['name'] = name
        self._personal_info['surname'] = surname
        
        if amount>0:
            self.__balance = amount
        elif amount == 0:
            raise ValueError('Amount must not be zero')
        self.__id = id
        self.pin=pin
    
    def deposit(self, amount):
        if amount>0:
            print("Operation in process...")
            sleep(2)
            self.__balance += amount
            print("your balance is ", self.__balance)
            return True
        else:
            print('Invalid amount')
            return False

    def withdraw(self, amount):
        if amount>0 and amount<self.__balance:
            print('Money transfering...')
            sleep(2) #delay 2 sec
            self.__balance -= amount
            print("Your balance now is ", self.__balance)
            return True
        else:
            print('Invalid amount')
            return False
            
    def check_balance(self):
        #do something
        print(f"Your balance is {self.__balance}")
        return self.__balance
    
    def verification(self):
        return self.__id
        
    
    
