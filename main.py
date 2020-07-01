from HeadQuarter import DemirBank
from Branch import DemirBankBranch
from Atm import DemirBankAtm

#Adil_account = DemirBank(name='Adil', surname='Adenov', id=7845, amount=50000)
#temp_account = DemirBankBranch(id_account=7845, object_account=Adil_account)

#temp_account.dep(30000, Adil_count)

#Saltanat = DemirBank(name='Saltanat', surname='Omuralieva', id=8088, amount=10000)
#Saltanat.check_balance()

#temp_account.transfer_money(Adil_account, Adil_account, 5200)
timur=DemirBank(name='Timur', surname='Abdraimov', id=1223, amount=1000, pin=5555)
atm  = DemirBankAtm(id_account=1223,object_account=timur)
atm.validation()
