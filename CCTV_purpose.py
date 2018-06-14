import csv

f1 = open('전국cctv표준데이터(1).csv')
f2 = open('전국cctv표준데이터(2).csv')
data1 = csv.reader(f1)
data2 = csv.reader(f2)
next(data1)
next(data2)
name = input('궁금한 지역을 입력해주세요 ex. 관악구 or 서초3동 : ')

purpose = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = ['교통단속', '교통정보수집', '기타', '다목적', 
          '도로방범', '도시공원', '불법주정차단속', '생활방범',
          '시설물관리', '쓰레기단속',' 쓰레기불법투기','어린이보호',
          '재난감시', '재난재해', '차량방범', '차번판독', '학교연계', 
          '경찰청', '교통방범', '구방범', '그린파킹', '마을방범', '무단투기',
          '물흘림', '방범용', '번호인식', '산불예방', '생활방범(파출소)',
          '시설관리', '시설물 관리', '시설물관리(문화재)', '쓰레기무단투기',
          '재난관리', '재난재해(산불감시)', '재난재해(수위관측)',
          '재난재해(재난감시)', '재난재해(적설관측)', '주차단속', '중학교',
          '청사관리', '청사내방범', '초등학교']
resultnum = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 11, 4, 4, 10, 12, 4, 7,
             13, 7, 9, 11, 3, 4, 11, 7, 8, 8, 8, 9, 11, 11, 11, 11, 11, 6, 10,
             3, 3, 10]
label = ['교통단속', '교통정보수집', '기타', '도로방범', '도시공원', 
         '불법주정차단속', '생활방범', '시설물관리', '쓰레기단속',
         '어린이보호', '재난감시', '경찰청', '그린파킹'] ##그래프값들

##해당 지역의 cctv 목적별로 분류 (개수)
for row in data1 :
    if name in row[2] :
        for i in range(len(result)) :
            if row[3] == result[i] :
                purpose[resultnum[i] - 1]  = purpose[resultnum[i] - 1] + int(row[4])

for row in data2 :
    if name in row[2] :
        for i in range(len(result)) :
            if row[3] == result[i] :
                purpose[resultnum[i] - 1] = purpose[resultnum[i] - 1] + int(row[4])


##그래프에서 0인값 제거
delindex = 0
sumi = 0
for i in range(len(result) - 1) : 
    if (purpose[delindex] == 0) :
        del label[delindex]
        del purpose[delindex]
    else : 
        delindex = delindex + 1
        
    if (len(purpose) == delindex) :
        break
        
for i in range(len(purpose)): 
    sumi = sumi + int(purpose[i])  
    
##원그래프 그리기
import matplotlib.pyplot as plt 
plt.figure(figsize=(6,4), dpi=400) 
plt.rc('font',family='Malgun Gothic') 
plt.title(name + '의 목적별 CCTV 현황 (전체 ' + str(sumi) + '개)')
plt.pie(purpose, labels = label, autopct='%1.1f%%', startangle = 90) 

plt.axis('equal') 
##plt.savefig(name + '_목적별')

##출력
for i in range(len(purpose)):
    print (label[i] + " : " + str(purpose[i]) + ' (' + str(round(purpose[i] * 100 / sumi, 1)) + '%)')
print ('전체 합계 = ' + str(sumi))
plt.show()"print('hello world')" 
