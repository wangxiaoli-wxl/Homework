#1.数学方面：五角数
import random
def getPentagonalNumber():
    n = ''
    for n in range(1,101):
        wujiaoshu =int(( n * ((3 * n) - 1)) / 2)
        print(wujiaoshu, end=' ') 
        if(n % 10 == 0):
            print("")#换行输出             
getPentagonalNumber()



#2.求一个整数各个数字之和
def sumDigits():
    num = float(input('请输入一个0~1000之间整数：'))
    ge = int(num / 100 )
    shi = int((num / 10 ) % 10)
    bai = int(num % 10)
    sum_ = ge + shi + bai
    print(sum_)
sumDigits()




#3.对三个数排序
def displaySortedNumbers():
    st=input("请输入三个整数").split()
    sb=[]
    for t in st:#转换序列st中的数字字串为整数
        sb.append(int(t))
        sb.sort()#排序
        print(sb)#输出
displaySortedNumbers()



#4.计算未来投资值
def futureInvestmentValue():
    investAmount = int(input("请输入投资额："))
    monthrate = float(input("请输入百分比格式的年利率：")) / 12
    years = 5
    for i in range(1,years + 1):
        futureInvestment = investAmount + (investAmount * monthrate *  i)
        print('未来值：%f'%futureInvestment)   
futureInvestmentValue()    
    

    
#5.显示字符：编写一个打印字符的函数
def printChars():
     for i in range(73,91):
        print(chr(i),end=" ")
        if i% 10 == 0:
            print("\n")
printChars()



#6.显示从2010年到2020年每年的天数
def numberOfDaysInAYear(year):
    for count in range(year,year+11):
        if count % 4 == 0 and count % 100 != 0 or count % 400 == 0:
            print("{}年有366天".format(count))
        else:
            print("{}年有365天".format(count))
numberOfDaysInAYear(2010)




#7.两点之间的距离
def distance(x1,x2,y1,y2):
    dis = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print("这两个点的距离是：%f"%dis)
distance(1,4,4,2)


#8.梅森素数(打出来不对)
def mei(p):
    c = []
    b = []
    for p in range(2,32):
        if p>1:
            for i in range(2,p):
                if (p % i) == 0:
                    break
                else:
                    d = 2**(p-1)
                    c.append([p,d])
        print(c)
mei(5)



#9.显示日期和时间
import time
def time_():
    localtime = time.asctime(time.localtime(time.time()))
    print('现在时间为：',localtime)
time_()


#10.掷骰子(else后不执行了？？？？？)
import random
def shaizi():
    a1 = random.choice([1,2,3,4,5,6])
    a2 = random.choice([1,2,3,4,5,6])
    if a1 + a2 == 2 or a1 + a2 == 3 or a1 + a2 == 12:
        print('a1:%d + a2:%d = %d'%(a1,a2,a1+a2))
        print('你输咯！继续努力')
    elif a1 + a2 == 7 or a1 + a2 == 11:
        print('a1:%d + a2:%d = %d'%(a1,a2,a1+a2))
        print('赢了，厉害了')
    else:
        print('a1:%d + a2:%d = %d'%(a1,a2,a1+a2))
        b1 = random.choice([1,2,3,4,5,6])
        b2 = random.choice([1,2,3,4,5,6])
        if b1 + b2 == 7:
            print('b1:%d + b2:%d = %d'%(b1,b2,b1+b2))
            print('输了')
        elif a1 + a2 == b1 + b2:
            print('b1:%d + b2:%d = %d'%(b1,b2,b1+b2))
            print('赢了')
shaizi()





