class Account:
    def __init__(self, account = {'account': None, 'money':-1}):
        self.accountlist = list()
        self.account = account
        
    # 계좌 불러오기
    def AccountlistCall(self):
        self.accountlist = list()
        f= open('0323/BANK/accounts.txt', 'r')
        lis = f.readlines()
        for li in lis :
            liar = li.split(',')
            saveAccount = {
                'account' : liar[0],
                'money' : int(liar[1])
            }
            self.accountlist.append(saveAccount)
        f.close()
    

    # 계좌 저장하기
    def AccountlistSave(self):
        self.AccountlistCall()
        f = open('0323/BANK/accounts.txt', "w")
        for x in self.accountlist:
            if self.account['account'] == x['account'] :
                x['money'] = self.account['money']
            f.write(f'{x['account']},{x['money']}\n')
        f.close()

    # 계좌 여부 확인하고 없으면 새로 생성하기
    def checkAccount(self):
        self.AccountlistCall()
        # print(self.accountlist)
        nums = input('계좌번호를 입력하세요 (x 업무 종료): ')
        if nums == 'x':
            self.account = {
                'account' : 'x'
            }
            return self.account
        check = False
        for i, x in enumerate(self.accountlist):
            if x['account'] == nums:
                check = True
                self.account = x
                break
        if not check :
            ans = input('해당 계좌는 없습니다. 계좌를 새로 만드시겠습니까?(y or n) : ')
            if ans == 'y':
                accountdic = {
                    'account' : nums,
                    'money' : 0
                }
                self.accountlist.append(accountdic)
                self.account = accountdic
                f = open('0323/BANK/accounts.txt','a')
                f.write(f'{self.account['account']},{self.account['money']}\n')
                f.close()
                f = open(f'0323/BANK/ACCOUNTS/{nums}.txt','w')
                f.close()
        return self.account