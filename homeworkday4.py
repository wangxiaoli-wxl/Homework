#1.编写一个程序读取成绩列表，并分级
def ScoreGrade()):
    list1=list(map(int,input('Please enter score:').split(',')))
    list2=sorted(list1)
    best=list2[-1]
    for i in range(0,len(list1)):
        if best>=list1[i]>=best-10:
            print('Student %d score is %d and grade is A !'%(i,list1[i]))
        elif best-10>list1[i]>=best-20:
            print('Student %d score is %d and grade is B !'%(i,list1[i]))
        elif best-20>list1[i]>=best-30:
            print('Student %d score is %d and grade is C !'%(i,list1[i]))
        elif best-30>list1[i]>=best-40:
            print('Student %d score is %d and grade is D !'%(i,list1[i]))
        else:
            print('Student %d score is %d and grade is E !'%(i,list1[i]))
if __name__ == '__main__':
    ScoreGrade()



#2.逆序读取数字
list_ = ['0','1','2','3','4','5','6','7','8','9']

list1 = list_[::-1]                    
print(list1)

list2 = sorted(list_,reverse=True)  
print(list2)



#3.统计数字个数
print("输入1-100之间的整数(以 0 结束):")
enterList=[] #记录输入的元素
while 1:
    a = int(input(">>>"))  #将输入转换为int型
    if a == 0:
        print ("你输入的是:",enterList)
        break  #结束输入
    if a<1 or a>100:  #限制只允许输入1到100之间的数
        print("Error!Please enter the numbers between 1 and 100!")
    else:
        enterList.append(a)
listVisited=[]  #保存列表中已经处理过的元素值，避免相同的值处理多次
for a in enterList:
    if a in listVisited: #已经处理过a，跳过此次循环
        break
    if enterList.count(a)>1:
        print("The number",a,"occurs",enterList.count(a),"times!")
    if enterList.count(a)==1:
        print("The number", a, "occurs",enterList.count(a), "time!")
    listVisited.append(a) #处理完a，把a 保存到这个列表中，以便下次跳过a的值



#4.分析成绩
def Statistics():
    list_=list(map(int,input('Please enter grade ：').split(' ')))
    total=0
    good=0
    for i in range(0,len(list_)):
        total += list_[i]
    average=total/len(list_)
    for grade in list_:
        if grade >= average:
            good+=1
    print('    The average score is %d '%average)
    print('   %d students with scores greater than or equal to the average score!'%good)
    print('   %d students with lower than average scores!'%(len(list_)-good))
if __name__ == '__main__':
    Statistics()

# #5.随机产生一串数字，然后统计每个数字个数
import numpy as np
import sys
sys.setrecursionlimit(100000)   #加大最大递归深度，否则会报错
NUM=0
LIST1=list(x for x in range(0,10))
LIST2=[]
counts=[0,0,0,0,0,0,0,0,0,0]
def Statistics():
    global LIST1,LIST2
    if len(LIST2) < 1000:
        List()
    else:
        for i in LIST2:
            counts[i]+=1
        print('1000个随机数中0~9的个数分别为',counts)    
def List():
    global NUM,LIST1,LIST2
    if NUM != 1000:
        LIST2.append(np.random.choice(LIST1))
        NUM += 1
        List()
    else:
        Statistics()
if __name__ == '__main__':
    Statistics()

# #6.输出最小元素的下标
def IndexOfSmallestElement():
    list1=list(map(int,input('Please enter a list of numbers:').split(',')))
    list2=sorted(list1)
    num=0
    for i in list1:
        if i==list2[0]:
            print('The subscript of the smallest element is：%d'%num)
        else:
            num+=1
if __name__ == '__main__':
    indexOfSmallestElement()




































