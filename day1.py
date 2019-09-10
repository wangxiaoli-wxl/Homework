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





  
