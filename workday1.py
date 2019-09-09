# 1.摄氏度转化为华氏度
# C = float(input('请输入摄氏度：'))
# F = (C * 1.8) + 32
# print('%.2f 摄氏度' %F)





# 2. 圆柱体面积体积
# import math
# radius = float(input('请输入圆的半径: '))
# high = float(input('请输入圆的高： '))
# area = math.pi * radius * radius
# volume = area * high
# print('面积: %.2f' % area)
# print('体积: %.2f' % volume)





# 3. 英尺换算米
# Foot = float(input('请输入英尺数：'))
# rice = 0.305 * Foot
# print('等于 %f 米' % rice) 





# 4. 计算能量
# import math
# M = float(input('请输入以千克为单位的水量：'))
# initial_temp = float(input('请输入初始温度：'))
# final_temp = float(input('请输入最终温度：'))
# Q = M * (final_temp - initial_temp) * 4184
# print('加热到此温度需要的能量为：%.1f ' % Q)





#5.计算利息 
# Difference = float(input('请输入差额：'))
# rate = float(input('请输入年利率：'))
# Interest = Difference * (rate / 1200)
# print('下个月要付的利息：%f' % Interest)





#6. 加速度
# Initial_velocity = float(input('请输入以m/s为单位的初始速度：'))
# Terminal_velocity = float(input('请输入以m/s为单位的末速度：'))
# time = float(input('请输入以s为单位的时间：'))
# a = (Terminal_velocity - Initial_velocity ) / time 
# print('加速度为：%.4f' % a)





#7. 复利值
# deposit = float(input('请输入每月存款金额：'))
# b = 1 + 0.00417
# a = [0]
# for i in range(6):
#     c = (100 + a[i]) * b  
#     a.append(c)
# print('六个月后的账户余额为：%.2f' % a[6])





#8.对一个整数中的各位数字求和
# integer = float(input('请输入一个0~1000之间的整数：'))
# bai = int(integer % 10)
# shi = int(integer /10 % 10)
# ge = int(integer /100)
# sum = ge + shi + bai
# print('各位数字之和：',sum)





#9.一个五边形的面积
# import math
# r = float(input('请输入一个顶点到中心的距离：'))
# s = 2 * r * math.sin(math.pi / 5)
# area = (5 * s * s) / (4 * math.tan(math.pi / 5))
# print('五边形面积为：%.2f' % area)
  



#10.五角形的面积
# import math
# s = float(input('请输入五角形的边长：'))
# area = (5 * (s ** 2)) / (4 * (math.tan(math.pi/5)))
# print('五角形的面积是：%f' % area)





#11.一个正多边形的面积
# import math
# n = float(input('请输入正多边形的边数：'))
# s = float(input('请输入正多边形的边长：'))
# area = (n * (s ** 2)) / (4 * (math.tan(math.pi/n)))
# print('%.0f 边形的面积为:%f' %(n,area))




#12.找出ASCII码的字符
# num = input('请输入一个字符：')
# a = int(input('请输入一个ASCII码:'))
# print( num + '的ASCII码为',ord(num))
# print( a , '对应的字符为',chr(a))






# qq = 'www.123.cn'
# for z in qq:
#     a = ord(z) 
#     print(a)




# year = int(input('请输入年份: '))
# if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#     print("闰年")
# else:
#     print("平年")




#判断月份
# Month = int(input('请输入月份： '))
# Year = int(input('请输入年份'))
# #31天的情况判断
# if (Month == 1 or Month == 3 or Month ==5 or Month == 7 or Month == 8
#         or Month == 10 or Month == 12):
#     print('本月31天')
# #30天的情况判断
# elif (Month == 4 or Month == 6 or Month ==9 or Month == 11):
#     print('本月30天')
# #闰年2月判断
# elif Month ==2 and ((Year % 4 == 0 and Year % 100 !=0 ) or Year % 400 == 0):
#     print('本月29天')
# #28天情况判断
# else:
#     print('本月28天')




#华氏温度--摄氏度
# F = float(input('请输入华氏温度: '))
# c = (F - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (F, c))





#水仙花
# num=int(input("请输入你要判断的正整数："))
# n=num
# sum=0
# length=len(str(num))
# while n!=0:
#     a=n%10
#     sum=sum+a**length
#     n=n//10
# if sum==num:
#     print(num,"是水仙花数")
# else:
#     print(num,"不是水仙花数")




#实现一个正方形(没成功)
# for i in range(10):
#     print('.',end="")
# print()
# for k in range(8):
#     print ('. ',' '*16,'. ',sep="")
# for j in range(10):
#     prin('. ',end="")





#正方形
# import turtle as t # 用别名来代替turtle库名调用
# t.pensize(2)# 设置线的大小
# for i in range(4): #因为有四条边，所以我们循环四次，即画四次
#     t.fd(100)# 每一次画100个像素
#     t.left(90)# 画100个像素之后转动90°
# t.done()# 停止画笔，结束绘图





#六边形
# import turtle
# turtle.pensize(2)#设置线的大小
# for i in range(6):#因为有六条边，所以我们画六次
#     turtle.fd(100)#前进100个像素单位
#     turtle.left(60)#向左旋转60度（每一个内角的外角都为60°）
# turtle.done()# 画布停留




# a = int(input('请输入第一个数：'))
# b = int(input('请输入第二个数：'))
# c = a - b 
# print(c,type(c))
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))




# #彩色蟒蛇
# import turtle
# def drawSnake(rad,angle,len,neckrad):
#     colors = ["red","orange","yellow","green","cyan","blue"]
#     for i in range(len):
#         turtle.color(colors[i])
#         turtle.circle(rad,angle)
#         turtle.circle(-rad,angle)
 
#     turtle.color("purple")
#     turtle.circle(rad,angle/2)
#     turtle.fd(rad)
#     turtle.circle(neckrad+1,180)
#     turtle.fd(rad*2/3)
 
# def main():
#     turtle.setup(1300,800,0,0)
#     turtle.penup()
#     turtle.goto(-350,0)
#     turtle.pendown()
#     pythonsize = 30
#     turtle.pensize(pythonsize)
#     turtle.seth(-40)
#     drawSnake(40,80,6,pythonsize/2)
 
# main()






  
import turtle
import math
  
def draw_polygon(aTurtle, size=50, n=3):
#   ''' 绘制正多边形
#   args:
#     aTurtle: turtle对象实例
#     size: int类型，正多边形的边长
#     n: int类型，是几边形    
#   '''
    for i in xrange(n):
        aTurtle.forward(size)
        aTurtle.left(360.0/n)
  
def draw_n_angle(aTurtle, size=50, num=5, color=None):
#   ''' 绘制正n角形，默认为黄色
#   args:
#     aTurtle: turtle对象实例
#     size: int类型，正多角形的边长
#     n: int类型，是几角形  
#     color: str， 图形颜色，默认不填色
#   '''
    if color:
        aTurtle.begin_fill()
        aTurtle.fillcolor(color)
    for i in xrange(num):
        aTurtle.forward(size)
        aTurtle.left(360.0/num)
        aTurtle.forward(size)
        aTurtle.right(2*360.0/num)
    if color:
        aTurtle.end_fill()
  
def draw_5_angle(aTurtle=None, start_pos=(0,0), end_pos=(0,10), radius=100, color=None):
#   ''' 根据起始位置、结束位置和外接圆半径画五角星
#   args:
#     aTurtle: turtle对象实例
#     start_pos: int的二元tuple，要画的五角星的外接圆圆心
#     end_pos: int的二元tuple，圆心指向的位置坐标点
#     radius: 五角星外接圆半径
#     color: str， 图形颜色，默认不填色  
#   '''
    aTurtle = aTurtle or turtle.Turtle()
    size = radius * math.sin(math.pi/5)/math.sin(math.pi*2/5)
    aTurtle.left(math.degrees(math.atan2(end_pos[1]-start_pos[1], end_pos[0]-start_pos[0])))
    aTurtle.penup()
    aTurtle.goto(start_pos)
    aTurtle.fd(radius)
    aTurtle.pendown()
    aTurtle.right(math.degrees(math.pi*9/10))
    draw_n_angle(aTurtle, size, 5, color)
  
def draw_5_star_flag(times=20.0):
#   ''' 绘制五星红旗
#   args:
#     times: 五星红旗的规格为30*20， times为倍数，默认大小为10倍， 即300*200
#   '''
    width, height = 30*times, 20*times
  # 初始化屏幕和海龟
    window = turtle.Screen()
    aTurtle = turtle.Turtle()
    aTurtle.hideturtle()
    aTurtle.speed(10)
  # 画红旗
    aTurtle.penup()
    aTurtle.goto(-width/2, height/2)
    aTurtle.pendown()
    aTurtle.begin_fill()
    aTurtle.fillcolor('red')
    aTurtle.fd(width)
    aTurtle.right(90)
    aTurtle.fd(height)
    aTurtle.right(90)
    aTurtle.fd(width)
    aTurtle.right(90)
    aTurtle.fd(height)
    aTurtle.right(90)  
    aTurtle.end_fill()
  # 画大星星
    draw_5_angle(aTurtle, start_pos=(-10*times, 5*times), end_pos=(-10*times, 8*times), radius=3*times, color='yellow') 
  # 画四个小星星
    stars_start_pos = [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]
for pos in stars_start_pos:
    draw_5_angle(aTurtle, start_pos=(pos[0]*times, pos[1]*times), end_pos=(-10*times, 5*times), radius=1*times, color='yellow') 
  # 点击关闭窗口
    window.exitonclick()
if __name__ == '__main__':
    draw_5_star_flag()



