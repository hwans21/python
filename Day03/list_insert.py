'''
1. append(): 요소를 리스트의 맨 마지막에 추가
2. insert(): 요소를 리스트의 특정 위치에 삽입
'''

nums=[1,3,5,7]
nums.append(9)
print(nums)

nums.append('안녕~')
print(nums)

# insert(index, value)
nums.insert(3,4)
print(nums)