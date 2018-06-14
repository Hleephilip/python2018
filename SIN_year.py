import csv

f = open('서울시범죄건수.csv')
data = csv.reader(f)

name = input('궁금한 서울시 지역을 입력해주세요 ex. 관악구 : ')

sins = [0, 0, 0, 0, 0, 0]
sinall = [0, 0, 0, 0, 0, 0]
label = ['2011년', '2012년', '2013년', '2014년',
        '2015년', '2016년']

sumi = 0

##해당 구
for row in data:
    if name in row[0] :
        for i in range(len(sins)):
            sins[i] = int(row[i + 1])
            sumi = sumi + int(sins[i])

    if row[0] == "평균" :
        for i in range(len(sins)):
            sinall[i] = int(row[i + 1])
            
##(꺾은선)그래프 그리기
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4), dpi=100) 
plt.rc('font',family='Malgun Gothic') 
plt.title(name + '의 연도별 범죄건수 (전체 ' + str(sumi) + '건)')
plt.xticks(range(len(label)), label, rotation = 45)
plt.ylabel('건')

plt.plot (sins, label = name)
plt.plot (sinall, label = '서울시')
plt.legend(loc = 2)
plt.show()
##print ('전체 합계 = ' + str(sumi))
##print ('전체 합계 = ' + str(sumi))