jomin = input('주민등록번호를 입력하세요: ')
print(f'주민등록번호 앞자리: {jomin[:6]}')
print(f'주민등록번호 뒷자리: {jomin[7:]}')
year = ''
gen = ''
month = ''
day = ''
age = ''
if(int(jomin[:2])>22):
    year = '19'
else:
    year = '20'

if(int(jomin[7])%2==0):
    gen = '여자'
else:
    gen = '남자'

if(int(jomin[2:4])<10):
    month=jomin[3]
else:
    month=jomin[2:4]

if(int(jomin[4:6])<10):
    day = jomin[5]
else:
    day = jomin[4:6]

age = 2021-int(year+jomin[0:2])-1

print(f'{year}{jomin[0:2]}년 {month}월 {day}일 {age}세 {gen}')

####################################################################

ssn = input('주민등록번호를 입력하세요: ')
# 921013-1234567

print('주민등록번호 앞자리:', ssn[:6])
print('주민등록번호 뒷자리:', ssn[7:])

year = int(ssn[:2])
month = ssn[2:4]
day = ssn[4:6]
gender_num = ssn[7]

if gender_num == '1' or gender_num == '3':
    gender = '남자'
else:
    gender = '여자'

birth_year = 0

if gender_num == '1' or gender_num == '2':
    birth_year = 1900 + year
else:
    birth_year = 2000 + year

age = 2021 - birth_year

print(f'{birth_year}년 {month}월 {day}일 {age}세 {gender}')
