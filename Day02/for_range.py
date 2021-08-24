'''
* 내장함수 range()

- 순차적으로 증가하는 정수의 순차적 자료형을 만들 때
대괄호 안에 데이터들을 콤마로 일일히 나열하는 것은 
한계가 있기 때문에, range함수를 사용하여 보다 수비게
순차형 반복 범위를 생성할 수 있습니다.

ex) range(begin,end,step)
- begin은 값이 포함되지만(이상),
 end는 값이 포함되지 않습니다(미만)
'''
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1)

list2 = list(range(1,11,1))
print(list2)

# step 생략 시 자동으로 1로 처리
list3 = list(range(4,15))
print(list3)

#range함수 괄호 안에 값을 한 개만 주면 end로 처리하고
#begin값을 자동으로 0으로 처리합니다.

list4 = list(range(5)) #list4 = list(range(0,5,1)) -> [0,1,2,3,4]
print(list4)

print('-'*40)

# 1~100까지의 누적합을 구하는 로직
total =0
for n in range(1,101):
    total +=n
print('1~100까지의 누적합:',total)

'''
- 정수를 하나 입력받아서 1부터 해당 수까지의 
모든 소수를 가로로 출력하고, 그 소수의 개수를 출력하시면 됩니다.
ex) 입력값: 12
    소수:2,3,5,7,11
    개수:5개
'''
flag = True
count=0
n = int(input('입력값: '))
print('소수:',end='')
for i in range(2,n+1):
    flag = True
    if i==2:
        count+=1
        print(i,end='')
    else:
        for t in range(2,i):
            if i%t==0:
                flag = False
        if flag:
            count+=1
            print(',',i,end='')
print('\n개수:',count,'개')