import csv

f1 = open('전국cctv표준데이터(1).csv')
f2 = open('전국cctv표준데이터(2).csv')
f3 = open('서울시범죄건수.csv')

sins = [0, 0, 0, 0, 0, 0]
label = ['2011년', '2012년', '2013년', '2014년',
        '2015년', '2016년']
data1 = csv.reader(f1)
data2 = csv.reader(f2)
data3 = csv.reader(f3)

next(data1)
next(data2)
name = input('궁금한 서울시 지역을 입력해주세요 ex. 관악구: ')

year = [0, 0, 0, 0, 0, 0]
result = [2011, 2012, 2013, 2014, 2015, 2016]
resultnum = [1, 2, 3, 4, 5, 6]
label = ['2011년', '2012년', '2013년', '2014년',
        '2015년', '2016년'] ##그래프값들


##해당 지역의 cctv 연도별로 분류 (개수)
for row in data1 :
    if name in row[2] :
        for i in range(len(result)) :
            mystring = str(row[8])
            if mystring[:4] == str(result[i]) :
                year[resultnum[i] - 1]  = year[resultnum[i] - 1] + int(row[4])

for row in data2 :
    if name in row[2] :
        for i in range(len(result)) :
            mystring = str(row[8])
            if mystring[:4] == str(result[i]) :
                year[resultnum[i] - 1]  = year[resultnum[i] - 1] + int(row[4])

sumi = 0

for i in range(len(year)): 
    sumi = sumi + int(year[i])
    
##해당 지역의 범죄율 DATA
for row in data3:
    if name in row[0] :
        for i in range(len(sins)):
            sins[i] = int(row[i + 1])
            
##막대그래프 그리기
import matplotlib.pyplot as plt ##기본 setting
plt.figure(figsize=(6,4), dpi=100) ##size와 해상도 조정
plt.rc('font',family='Malgun Gothic') ##한글 글꼴 지정|
plt.title(name + '의 연도별 CCTV와 범죄율')##제목 설정
plt.xticks(range(len(label)), label, rotation = 45) #x축 레이블
plt.bar(label, year, color = 'green') ##plot 이라 쓰지 않고 bar라고 막대그래프는 쓴다.
        ##x값      ##막대 크기     ##원한다면 color 설정
plt.plot (sins, label = name)
plt.legend(loc = 2)

##데이터 레이블 첨부
for i in range(len(year)) :
    if year[i] != 0 :
        plt.annotate(year[i], xy=(-0.25 + i,year[i]), fontsize=10, horizontalalignment='middle')
plt.show()

for i in range(len(year)):
    print (label[i] + " : " + str(year[i]) + ' (' + str(round(year[i] * 100 / sumi, 1)) + '%)')
print ('전체 합계 = ' + str(sumi))