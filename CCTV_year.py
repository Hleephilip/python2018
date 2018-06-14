import csv

f1 = open('����cctvǥ�ص�����(1).csv')
f2 = open('����cctvǥ�ص�����(2).csv')
data1 = csv.reader(f1)
data2 = csv.reader(f2)
next(data1)
next(data2)
name = input('�ñ��� ������ �Է����ּ��� ex. ���Ǳ� or ����3�� : ')

year = [0, 0, 0, 0, 0, 0, 0, 0]
result = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
resultnum = [1, 2, 3, 4, 5, 6, 7, 8]
label = ['2010��', '2011��', '2012��', '2013��', '2014��',
        '2015��', '2016��', '2017��'] ##�׷�������


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
    
##����׷��� �׸���
import matplotlib.pyplot as plt 
plt.figure(figsize=(6,4), dpi=100) 
plt.rc('font',family='Malgun Gothic') 
plt.title(name + '�� ������ CCTV ��Ȳ (���, ��ü ' + str(sumi) + '��)')
plt.bar(label, year, color = 'green') 

##������ ���̺� ÷��
for i in range(len(year)) :
    if year[i] != 0 :
        plt.annotate(year[i], xy=(-0.25 + i,year[i]), fontsize=10, horizontalalignment='middle')
plt.show()

for i in range(len(year)):
    print (label[i] + " : " + str(year[i]) + ' (' + str(round(year[i] * 100 / sumi, 1)) + '%)')
print ('��ü �հ� = ' + str(sumi))
plt.show()