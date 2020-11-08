for i in range(10): # -> 0부터 9까지 10번 반복
    globals()['househap{}'.format(i)] = []

userInput = ''

ziphap = int(input('집합의 개수: '))
for i in range(ziphap): # -> 0부터 9까지 10번 반복
    globals()['househap{}'.format(i)] = set()

for i in range(ziphap):
  print('[*] ', i+1, '번째 집합입니다.')
  while userInput != 000:
    userInput = int(input('집합 원소: '))
    if userInput != 000 or userInput == None:
      globals()['househap{}'.format(i)].add(int(userInput))
  userInput = ''
  print('\n')


print('\n')

while userInput != 0:
  for i in range(ziphap):
    print('[!]', i+1, '번째 집합: ', globals()['househap{}'.format(i)])
  print('============================================')
  print('[+] 0 입력: 프로그램 종료')
  print('[+] 1 입력: 교집합 구하기')
  print('[+] 2 입력: 합집합 구하기')
  print('[+] 3 입력: 차집합 구하기')
  print('[+] 4 입력: 부분집합의 개수 구하기')
  print('[+] 5 입력: 진부분집합의 개수 구하기')
  print('[+] 6 입력: 포함하지 않는 조건이 있는 집합의 개수 구하기')
  print('[+] 7 입력: 반드시 포함하는 조건이 있는 집합의 개수 구하기')
  print('[+] 8 입력: 적어도 하나를 포함하는 조건이 있는 집합의 개수 구하기')
  print('============================================')
  userInput = int(input('[?] 원하는 메뉴의 숫자 입력: '))
  print('\n\n')
  if userInput == 0:
    # 프로그램 종료
    print('[!] 프로그램을 종료합니다.')
  elif userInput == 1:
    # 교집합 구하기
    userInputA = int(input('[?] 몇 번째 집합에서 교집합을 구할까요? (1/2) : '))-1
    userInputB = int(input('[?] 몇 번째 집합에서 교집합을 구할까요? (2/2) : '))-1
    cal_result = globals()['househap{}'.format(userInputA)]&globals()['househap{}'.format(userInputB)]
    if cal_result == set():
      cal_result = ('Ø(공집합)')
    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('[!] ', userInputA+1, '번째 집합과 ', userInputB+1, '번째 집합에서의 교집합은 ', cal_result, ' 입니다!')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n')
  elif userInput == 2:
    # 합집합 구하기
    userInputA = int(input('[?] 몇 번째 집합에서 합집합을 구할까요? (1/2) : '))-1
    userInputB = int(input('[?] 몇 번째 집합에서 합집합을 구할까요? (2/2) : '))-1
    cal_result = globals()['househap{}'.format(userInputA)]|globals()['househap{}'.format(userInputB)]
    if cal_result == set():
      cal_result = ('Ø(공집합)')
    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('[!] ', userInputA+1, '번째 집합과 ', userInputB+1, '번째 집합에서의 합집합은 ', cal_result, ' 입니다!')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n')
  elif userInput == 3:
    # 차집합 구하기
    userInputA = int(input('[?] 몇 번째 집합에서 차집합을 구할까요? (1/2) : '))-1
    userInputB = int(input('[?] 몇 번째 집합에서 차집합을 구할까요? (2/2) : '))-1
    cal_result = globals()['househap{}'.format(userInputA)]-globals()['househap{}'.format(userInputB)]
    if cal_result == set():
      cal_result = ('Ø(공집합)')
    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('[!] ', userInputA+1, '번째 집합과 ', userInputB+1, '번째 집합에서의 차집합은 ', cal_result, ' 입니다!')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n')
  elif userInput == 4:
    # 부분집합 개수 구하기
    userInputA = int(input('[?] 몇 번째 집합에서 부분집합의 개수를 구할까요? (1/1) : '))-1
    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('[!] ', userInputA+1, '번째 집합의 부분집합 개수는 ', 2**len(globals()['househap{}'.format(userInputA)]), ' 개 입니다!')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n')
  elif userInput == 5:
    # 진부분집합 개수 구하기
    userInputA = int(input('[?] 몇 번째 집합에서 진부분집합의 개수를 구할까요? (1/1) : '))-1
    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('[!] ', userInputA+1, '번째 집합의 부분집합 개수는 ', 2**len(globals()['househap{}'.format(userInputA)])-1, ' 개 입니다!')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n')
  elif userInput == 6:
    # 포함하지 않는 조건이 있는 집합의 개수  구하기
    userInputA = int(input('[?] 몇 번째 부분집합에서 포함하지 않는 조건이 있는 집합의 개수를 구할까요? (1/1) : '))-1
    userInputB = int(input('[?] 몇 개의 수가 포함되지 않아야 하나요? (1/1) : '))
    cal_result = 2**(len(globals()['househap{}'.format(userInputA)])-userInputB)
    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('[!] ', userInputA+1, '번째 부분집합에서 ', userInputB, ' 개를 포함하지 않는 조건이 있는 집합의 개수 개수는 ', cal_result, ' 개 입니다!')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n')
  elif userInput == 7:
    # 반드시 포함하는 조건이 있는 집합의 개수  구하기
    userInputA = int(input('[?] 몇 번째 부분집합에서 반드시 포함되어야 하는 조건이 있는 집합의 개수를 구할까요? (1/1) : '))-1
    userInputB = int(input('[?] 몇 개의 수가 반드시 포함되어야 하나요? (1/1) : '))
    cal_result = 2**(len(globals()['househap{}'.format(userInputA)])-userInputB)
    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('[!] ', userInputA+1, '번째 부분집합에서 ', userInputB, ' 개를 반드시 포함하는 조건이 있는 집합의 개수 개수는 ', cal_result, ' 개 입니다!')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n')
  elif userInput == 8:
    # 적어도 하나를 포함하는 조건이 있는 집합의 개수 구하기
    userInputA = int(input('[?] 몇 번째 부분집합에서 적어도 하나를 포함되어야 하는 조건이 있는 집합의 개수를 구할까요? (1/1) : '))-1
    userInputB = int(input('[?] 몇 개의 수가 반드시 포함되어야 하나요? (1/1) : '))
    cal_result = 2**(len(globals()['househap{}'.format(userInputA)])) - 2**(len(globals()['househap{}'.format(userInputA)])-userInputB)
    print('\n')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('[!] ', userInputA+1, '번째 부분집합에서 ', userInputB, ' 개를 반드시 포함하는 조건이 있는 집합의 개수 개수는 ', cal_result, ' 개 입니다!')
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\n')
  else:
    print('[X] 잘못된 입력입니다.')
  


'''

print('교집합: ', a&b)
print('합집합: ', a|b)
print('차집합: ', a-b)
print(len(a))   # 집합 a 의 개수

문제: 짱 중요한 수학 유형(하) 28p 9번문제

집합 A = {x|x는 9 이하의 홀수}의 부분집합 중에서
다음 조건을 만족하는 집합 X의 개수는?

(가) 1
(나) 3

'''

''''
aa = set()

a = 1   # 0으로 설정할 경우 아래에서 0을 계산해야 함
while ( a <= 9):
    if (a%2) != 0:  # 홀수/짝수를 구분하기 위해서(9 이하의 홀수) a 값을 2로 나누었을때 나머지가 0이 아니라면(짝수가 아니라면)
        print('집합 A의 조건에 해당하는 수: ', a)    # 사용자에게 추가되었음을 알리고
        aa.add(a)
    a = a+1

print('집합 A: ', aa)
# (가) 조건

print('정답 : ',2**(len(aa)-1-2))
'''
