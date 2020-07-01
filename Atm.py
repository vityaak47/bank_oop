from HeadQuarter import DemirBank

class DemirBankAtm(DemirBank):
    
    
    def __init__(self, id_account, object_account):
        self.object_account=object_account
        self.id = object_account.verification()
        if self.id != id_account:
            raise TypeError('Verification Error')
        else:
            print("Verification passed")
            
    def validation(self):   
        pin=int(input('enter your pin:'))
        if pin==self.object_account.pin:
            print('Welcome')
            print('1.withdraw')
            choice=int(input('enter your choice:'))
            if choice==1:
            
                amt=int(input('Enter your amount:'))
                
                return self.object_account.withdraw(amt)
               
                
        else:
            print('wrong pin')
    
    

            