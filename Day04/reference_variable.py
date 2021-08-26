a=3
b=a
print(a,b)

a=5
print(a,b)

list1 = [1,2,3]
list2 = list1
print(list1,list2)

list1[0]=4
print(list1,list2)

print('list1주소값: ',id(list1))
print('list2주소값: ',id(list2))

print('-'*40)
list1 = [1,2,3]
list2 = []
list2 = list1.copy() # 리스트 내부 요소들을 복사하여 전달

list1[0]=4
print(list1,list2)