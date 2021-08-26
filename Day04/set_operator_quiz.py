
'''
- 서로 다른 정수가 담긴 두 개의 리스트를 비교하여
li 안에 있는 정수가 li2에도 담겨있다면 그 정수를 배제하세요
서로 겹치지 않는 정수만 담긴 새로운 리스트를 생성해 보세요
'''

li=[1,2,3,4,5,6,7]
li2 = [1,3,8,4,5,7,101]
result = []

for x in li:
    bool = True
    for y in li2:
        if x == y:
            bool = False
            break
    if bool == True:
        result.append(x)
for x in li2:
    bool = True
    for y in li:
        if x == y:
            bool = False
            break
    if bool == True:
        result.append(x)

print(result)
######################################
li3=[]
for n in li:
    if n not in li2:
        li3.append(n)
for n in li2:
    if n not in li:
        li3.append(n)
print(li3)
################################
result = set(li)^ set(li2)
print(result)
