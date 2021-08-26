import random as r

correct = r.randint(1,100)
count = 0
while True:
    num = int(input('정수를 입력해주세요: '))
    if correct > num:
        print('UP!')
    elif correct < num:
        print('DOWN!')
    else:
        print('정답입니다.~~~')
        count+=1
        break;
    count+=1
print(f'{count}번 만에 정답을 맞추셨습니다.')