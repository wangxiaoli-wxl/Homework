#1.解一元二次方程
import math
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))
if a != 0:
    delta = b**2-4*a*c
    if delta < 0:
        print("无根")
    elif delta == 0:
        s = -b/(2*a)
        print("唯一根x=",s)
    else :
        root = math.sqrt(delta)
        x1 = (-b+root)/(2*a)
        x2 = (-b-root)/(2*a)
        print("x1=",x1,"\t","x2=",x2)



#2.学习加法
import math
import random
n = random.randint(1,100)
print(n)
m = random.randint(1,100)
print(m)
n1 = float(input('%d+%d = '%(n,m)))
if n1 == n + m:
    print('True')
else:
    print('False')



#3.找未来数据

today = int(input('输入今天是星期几：'))
count = int(input('到未来的天数：'))
fd= count%7
b= today+fd
c= b%7
print('今天是星期%d,%d天后是星期%d'%(today,count,c))
# #



#4.对三个整数排列
a = [88,77,66]
a.sort()
print(a)



#5.比较价钱
money1 = float(input('请输入第一种大米的价钱：'))
weight1 = float(input('请输入第一种大米的重量：'))
money2 = float(input('请输入第二种大米的价钱：'))
weight2 = float(input('请输入第二种大米的重量：'))
dan1 = money1 / weight1
dan2 = money2 / weight2
if dan1 > dan2:
    print('第二种大米价钱更实惠')
elif dan1 < dan2:
    print('第一种大米价钱更实惠')
else:
    print('两种大米价格相同')

    


#6.找出一个月中的天数

Year = int(input('请输入年份'))
Month = int(input('请输入月份： '))
#31天的情况判断
if (Month == 1 or Month == 3 or Month ==5 or Month == 7 or Month == 8
        or Month == 10 or Month == 12):
    print('本月31天')
#30天的情况判断
elif (Month == 4 or Month == 6 or Month ==9 or Month == 11):
    print('本月30天')
#闰年2月判断
elif Month ==2 and ((Year % 4 == 0 and Year % 100 !=0 ) or Year % 400 == 0):
    print('本月29天')
#28天情况判断
else:
    print('本月28天')




#7.游戏：头或尾
import random
n = float(input('你猜测的结果是（1:正面,2:反面):'))
tan = random.randint(1,2)
print('硬币抛出%d'%tan)
if 'tan' == 'n':
    print('哎呦！不错哟')
else:
    print('猜错喽！再接再厉')



#8.剪刀石头布
import random
sci = float(input('你出什么？(1-石头，2-剪刀，3-布)：'))
com = random.randint(1,3)
print('电脑出%d'%com)
if sci == com:
    print('平局')
elif sci == '1' and com == '2':
    print('你赢了')
elif sci == '1' and com == '3':
    print('电脑赢了')
else:
    print('你很出色！')
    

#9.一周的星期几
import math
y = int(input('请输入年份：'))
m = int(input('请输入月份：'))
q = int(input('请输入哪一天：'))
a = ['周六','周日','周一','周二','周三','周四','周五']
if m == 1:
    m ==13
    y = y - 1
if m == 2:
    m =14
    y = y - 1
h = int(q + ((26 * (m + 1)) // 10) + (y%100) + ((y%100) / 4)+((y//100) / 4) + 5 * (y//100)) % 7
day = a[h]
print('%s年%s月%s号是%s'%(y,m,q,day))




#10.游戏：选出一张牌
import numpy as np 
paimian = np.random.choice(['A','2','3','4','5','6','7','8','9','10','j','q','k'])
huase = np.random.choice(['红桃','方片','梅花','黑桃'])
print('你选择的是',huase,paimian)



#11.回文数
num = input('请输入一个任意数：')
if num == num[::-1]:
    print ('这是一个回文数')
else:
    print ('这不是一个回文数')



#12.计算三角形的周长
import math
d1 = float(input('请输入三角形第一条边的长：'))
d2 = float(input('请输入三角形第二条边的长：'))
d3 = float(input('请输入三角形第三条边的长：'))
if (d1 + d2) > d3 or (d1 + d3) > d2 or (d3 + d2) > d1:
    s = d1 + d2 + d3
    print('三角形边长为：%.1f'% s)
else:
    print('输入边长不对')




#13.统计正数和负数的个数然后计算这些数的平均值
i = 0
j = 0
sum_zheng = 0
sum_fu = 0
i = input('除了0的其他数(以0结束)：')
while i != '0':
    if i < '0':
        sum_fu += int(i)
    else:
        sum_zheng += int(i)
    i = input('除了0的其他数(以0结束)：')
    j +=1
print('正数平均值%.0f'%sum_zheng , '负数平均值%.0f'%sum_fu,j)



 #14.计算未来学费
import math
si = 0
s = 10000
for i in range(13):
    s = s * 0.05 + s
    if i == 9:
        print('十年后的学费是:%d'%s)
    if i >= 9:
        si += s
        print('十年后大学四年的总学费:%d'%si)




#15.找出可被5和6 同时整除的数
count = 0
for i in range(100,1000):
    if i % 5 == 0 and i % 6 == 0:
        print(i,end = "  ")
        count += 1
    if count % 10 == 0:
        print(end='  ')



#16.找出最小的n满足n的二次幂>12000
n = 1
while n ** 2 < 12000:
    n += 1
    print(n)

n = 1
while n ** 3 < 12000:
    n += 1
    print(n-1)











