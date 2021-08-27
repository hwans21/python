'''
* points.txt 파일의 숫자값을 모두 읽어서
총합과 평균을 구한 뒤
총점, 평균값을 result.txt라는 파일에
쓰는 프로그램을 작성해 보세요.
'''
import traceback as trace
try:
    f = open('c:/test/points.txt','r')
    points = f.readline().split()
    sum = 0
    for p in points:
        sum+=int(p)
    avg = sum/len(points)
    f = open('c:/test/result.txt', 'w')
    text = f'총합: {sum}, 평균: {avg:0.2f}'
    f.write(text)
    print('파일 저장 성공!')
except:
    print('파일 저장 실패!')
    print(trace.format_exc())
finally:
    f.close()