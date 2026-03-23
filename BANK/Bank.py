# 입출금 여부 선택
# 계좌번호 입력
# Accountlist 에서 계좌번호 찾기
# 없으면 새로 만들기
# 찾으면 acnt = Accountlist[i]
# 입금액, 출금액 입력
# 잔고에 반영(출금의 경우, 잔고보다 많이 출금하려고 하면 경고 발생)
# 방금 처리한 내역(계좌번호, 입금액 or 출금액 xxxx)

# 거래내역 보기
# 계좌번호 입력
# Accountlist에서 계좌번호 찾기
# 없으면 없는 계좌입니다. 
# 찾으면 출력
# 업무 종료 - 업무종료합니다. break
# ============================================================================================

from Account import Account
from Accountinout import Accountinout

while True:

    print('i: 입금')
    print('o: 출금')
    print('d: 거래내역보기')
    print('x: 업무 종료')
    ans = input('업무 선택 : ')
    if ans == 'x':
        print('업무를 종료합니다.')
        break
    elif ans != 'i' and ans !='o' and ans!='d':
        print('잘못 입력하셨습니다. 다시 입력해주세요.')
        continue

    account = Account().checkAccount()
    # print(account)
    if account['account'] == None:
        print('해당 계좌가 없습니다. 다시 입력해주세요.')
        continue
    accInout = Accountinout(account)

    if ans == 'i': #입금
        accInout.accountinput()
    elif ans == 'o': #출금
        accInout.accountoutput()
    elif ans == 'd': #거래내역 보기
        accInout.display()