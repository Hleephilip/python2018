import csv

f = open('����ù��˰Ǽ�.csv')
data = csv.reader(f)

name = input('�ñ��� ����� ������ �Է����ּ��� ex. ���Ǳ� : ')

sins = [0, 0, 0, 0, 0, 0]
sinall = [0, 0, 0, 0, 0, 0]
label = ['2011��', '2012��', '2013��', '2014��',
        '2015��', '2016��']

sumi = 0

##�ش� ��
for row in data:
    if name in row[0] :
        for i in range(len(sins)):
            sins[i] = int(row[i + 1])
            sumi = sumi + int(sins[i])

    if row[0] == "���" :
        for i in range(len(sins)):
            sinall[i] = int(row[i + 1])
            
##(������)�׷��� �׸���
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4), dpi=100) 
plt.rc('font',family='Malgun Gothic') 
plt.title(name + '�� ������ ���˰Ǽ� (��ü ' + str(sumi) + '��)')
plt.xticks(range(len(label)), label, rotation = 45)
plt.ylabel('��')

plt.plot (sins, label = name)
plt.plot (sinall, label = '�����')
plt.legend(loc = 2)
plt.show()
##print ('��ü �հ� = ' + str(sumi))
##print ('��ü �հ� = ' + str(sumi))