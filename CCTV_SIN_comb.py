import csv

f1 = open('����cctvǥ�ص�����(1).csv')
f2 = open('����cctvǥ�ص�����(2).csv')
f3 = open('����ù��˰Ǽ�.csv')

sins = [0, 0, 0, 0, 0, 0]
label = ['2011��', '2012��', '2013��', '2014��',
        '2015��', '2016��']
data1 = csv.reader(f1)
data2 = csv.reader(f2)
data3 = csv.reader(f3)

next(data1)
next(data2)
name = input('�ñ��� ����� ������ �Է����ּ��� ex. ���Ǳ�: ')

year = [0, 0, 0, 0, 0, 0]
result = [2011, 2012, 2013, 2014, 2015, 2016]
resultnum = [1, 2, 3, 4, 5, 6]
label = ['2011��', '2012��', '2013��', '2014��',
        '2015��', '2016��'] ##�׷�������


##�ش� ������ cctv �������� �з� (����)
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
    
##�ش� ������ ������ DATA
for row in data3:
    if name in row[0] :
        for i in range(len(sins)):
            sins[i] = int(row[i + 1])
            
##����׷��� �׸���
import matplotlib.pyplot as plt ##�⺻ setting
plt.figure(figsize=(6,4), dpi=100) ##size�� �ػ� ����
plt.rc('font',family='Malgun Gothic') ##�ѱ� �۲� ����|
plt.title(name + '�� ������ CCTV�� ������')##���� ����
plt.xticks(range(len(label)), label, rotation = 45) #x�� ���̺�
plt.bar(label, year, color = 'green') ##plot �̶� ���� �ʰ� bar��� ����׷����� ����.
        ##x��      ##���� ũ��     ##���Ѵٸ� color ����
plt.plot (sins, label = name)
plt.legend(loc = 2)

##������ ���̺� ÷��
for i in range(len(year)) :
    if year[i] != 0 :
        plt.annotate(year[i], xy=(-0.25 + i,year[i]), fontsize=10, horizontalalignment='middle')
plt.show()

for i in range(len(year)):
    print (label[i] + " : " + str(year[i]) + ' (' + str(round(year[i] * 100 / sumi, 1)) + '%)')
print ('��ü �հ� = ' + str(sumi))