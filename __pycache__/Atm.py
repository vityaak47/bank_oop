from HeadQuarter import DemirBank

class DemirBankAtm(DemirBank):
#withdraw
    
    def __init__(self, id_account, object_account):
        self.id = object_account.verification()
        if self.id != id_account:
            raise TypeError('Verification Error')
        else:
            print("Verification passed")

     def dep(self, amount, object_account):
        return object_account.deposit(amount)