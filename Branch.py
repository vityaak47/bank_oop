from HeadQuarter import DemirBank


class DemirBankBranch(DemirBank):
#deposit 
#withdraw
#Transfer    
    
    def __init__(self, id_account, object_account):
        self.id = object_account.verification()
        if self.id != id_account:
            raise TypeError('Verification Error')
        else:
            print("Verification passed")
    
    def dep(self, amount, object_account):
        return object_account.deposit(amount)
    
    def transfer_money(self, object_account_from, object_account_to, amount):
        if object_account_from.withdraw(amount) and object_account_to.deposit(amount): #and, True, True            
            print("Transfer passed")
            
    
        else:
            print("Transfer Error")
            


