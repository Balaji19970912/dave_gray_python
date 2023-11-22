from bank_accounts import *

Luffy = BankAccount(1000,'Luffy')
Zoro = BankAccount(2000,'Zoro')

Luffy.getBalance()
Luffy.deposit(500)

Luffy.withdraw(10000)

Luffy.transfer(10000, Zoro)
Luffy.transfer(100, Zoro)

Sanji = InterestRewardsAcct(1000,"Sanji")

Sanji.getBalance()
Sanji.deposit(100)

Sanji.transfer(100,Zoro)

Nami = SavingsAcct(1000,"Nami")

Nami.getBalance()

Nami.deposit(100)

Nami.transfer(150,Luffy)