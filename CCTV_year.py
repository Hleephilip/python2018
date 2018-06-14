import csv

f1 = open('전국cctv표준데이터(1).csv')
f2 = open('전국cctv표준데이터(2).csv')
data1 = csv.reader(f1)
data2 = csv.reader(f2)
next(data1)
next(data2)
name = input('궁금한 지역을 입력해주세요 ex. 관악구 or 서초3동 : ')

year = [0, 0, 0, 0, 0, 0, 0, 0]
result = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
resultnum = [1, 2, 3, 4, 5, 6, 7, 8]
label = ['2010년', '2011년', '2012년', '2013년', '2014년',
        '2015년', '2016년', '2017년'] ##그래프값들


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
    
##막대그래프 그리기
import matplotlib.pyplot as plt 
plt.figure(figsize=(6,4), dpi=100) 
plt.rc('font',family='Malgun Gothic') 
plt.title(name + '의 연도별 CCTV 현황 (대수, 전체 ' + str(sumi) + '개)')
plt.bar(label, year, color = 'green') 

##데이터 레이블 첨부
for i in range(len(year)) :
    if year[i] != 0 :
        plt.annotate(year[i], xy=(-0.25 + i,year[i]), fontsize=10, horizontalalignment='middle')
plt.show()

for i in range(len(year)):
    print (label[i] + " : " + str(year[i]) + ' (' + str(round(year[i] * 100 / sumi, 1)) + '%)')
print ('전체 합계 = ' + str(sumi))
plt.show()