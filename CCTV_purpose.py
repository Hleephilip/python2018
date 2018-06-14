import csv

f1 = open('����cctvǥ�ص�����(1).csv')
f2 = open('����cctvǥ�ص�����(2).csv')
data1 = csv.reader(f1)
data2 = csv.reader(f2)
next(data1)
next(data2)
name = input('�ñ��� ������ �Է����ּ��� ex. ���Ǳ� or ����3�� : ')

purpose = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = ['����ܼ�', '������������', '��Ÿ', '�ٸ���', 
          '���ι��', '���ð���', '�ҹ��������ܼ�', '��Ȱ���',
          '�ü�������', '������ܼ�',' ������ҹ�����','��̺�ȣ',
          '�糭����', '�糭����', '�������', '�����ǵ�', '�б�����', 
          '����û', '������', '�����', '�׸���ŷ', '�������', '��������',
          '���긲', '�����', '��ȣ�ν�', '��ҿ���', '��Ȱ���(�����)',
          '�ü�����', '�ü��� ����', '�ü�������(��ȭ��)', '�����⹫������',
          '�糭����', '�糭����(��Ұ���)', '�糭����(��������)',
          '�糭����(�糭����)', '�糭����(��������)', '�����ܼ�', '���б�',
          'û�����', 'û�系���', '�ʵ��б�']
resultnum = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 11, 4, 4, 10, 12, 4, 7,
             13, 7, 9, 11, 3, 4, 11, 7, 8, 8, 8, 9, 11, 11, 11, 11, 11, 6, 10,
             3, 3, 10]
label = ['����ܼ�', '������������', '��Ÿ', '���ι��', '���ð���', 
         '�ҹ��������ܼ�', '��Ȱ���', '�ü�������', '������ܼ�',
         '��̺�ȣ', '�糭����', '����û', '�׸���ŷ'] ##�׷�������

##�ش� ������ cctv �������� �з� (����)
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


##�׷������� 0�ΰ� ����
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
    
##���׷��� �׸���
import matplotlib.pyplot as plt 
plt.figure(figsize=(6,4), dpi=400) 
plt.rc('font',family='Malgun Gothic') 
plt.title(name + '�� ������ CCTV ��Ȳ (��ü ' + str(sumi) + '��)')
plt.pie(purpose, labels = label, autopct='%1.1f%%', startangle = 90) 

plt.axis('equal') 
##plt.savefig(name + '_������')

##���
for i in range(len(purpose)):
    print (label[i] + " : " + str(purpose[i]) + ' (' + str(round(purpose[i] * 100 / sumi, 1)) + '%)')
print ('��ü �հ� = ' + str(sumi))
plt.show()"print('hello world')" 
