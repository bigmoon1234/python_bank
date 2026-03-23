from Account import Account
from text import line
import time

class Accountinout:
    def __init__(self, account):
        self.account = account

    def chnum(self, ans):
        while True:
            num = input(f'{ans}할 금액을 입력하세요 : ')
            if num == 'x':
                print(f'{ans}를 취소합니다.')
                return -1
            try:
                return int(num)
            except ValueError:
                print('입금할 금액을 잘못 입력하셨습니다. 다시 입력해주세요!')

    def accountinput(self):
        num = self.chnum('입금')
        if num == -1: return
        self.account['money'] +=num
        print(f'입금이 완료되었습니다. 잔고 : {self.account['money']}원')
        # print(self.account)
        Account(self.account).AccountlistSave()
        f = open(f'0323/BANK/ACCOUNTS/{self.account['account']}.txt', 'a')
        f.write(f'{time.asctime(time.localtime(time.time()))},입금,{num},{self.account['money']}\n')
        f.close()
    
    def accountoutput(self):
        num = self.chnum('출금')
        if num == -1: return
        if self.account['money'] < num :
            print('잔고가 부족합니다. 해당 출금을 취소합니다.')
            return
        self.account['money'] -= num
        print(f'출금이 완료되었습니다. 잔고 : {self.account['money']}원')
        Account(self.account).AccountlistSave()
        f = open(f'0323/BANK/ACCOUNTS/{self.account['account']}.txt', 'a')
        f.write(f'{time.asctime(time.localtime(time.time()))},출금,{num},{self.account['money']}\n')
        f.close()

    def display(self):
        f = open(f'0323/BANK/ACCOUNTS/{self.account['account']}.txt','r')
        lis = f.readlines()
        for li in lis:
            res = li.split(',')
            res[3] = int(res[3])
            print(f'{res[0]} __ {res[1]} :  {res[2]}원         ...  잔액 : {res[3]}원')
        line()
        print(' '*50,f'...총 잔액 : {self.account['money']}원')