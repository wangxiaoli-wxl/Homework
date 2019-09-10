# import hashlib
# m = hashlib.md5
# a = input('请输入字符串：')
# m.update(bytes(a, encoding='utf8'))
# print(m.hexdigest())



# username = input('请输入用户名：')
# password = input('请输入密码：')
# if username == 'admin' and password == '12345':
#     print('登陆成功')
# else:
#     print('登陆失败，用户名或密码错误')



#分数等级
# s = float(input('请输入分数：'))
# if s >= 80:
#     print('A')
# elif s >= 70 and s <= 80:
#     print('B')
# elif s >= 60 and s <= 70:
#     print('C')
# else:
#     print('D')



#账号注册






#公式
# x = float(input('请输入x:'))
# if x > 1:
#     print( 3*x - 5)
# elif -1<=x<=1:
#     print(x+2) 
# else :
#     print(5*x+3)




#计算器
# num1 = float(input('请输入第一个数字：'))
# num2 = float(input('请输入第二个数字：'))
# symbol = input('请输入运算符号（+-*/）:')
# if symbol == '+':
#     print('%.1f+%.1f=%.1f'%(num1,num2,num1+num2))
# elif symbol == '-':
#     print('%.1f-%.1f=%.1f'%(num1,num2,num1-num2))
# elif symbol == '*':
#     print('%.1f*%.1f=%.1f'%(num1,num2,num1*num2))
# elif symbol == '/':
#     print('%.1f/%.1f=%.1f'%(num1,num2,num1/num2))
# else:
#     print('输入的符号不对')




#石头剪刀布
# import numpy as np

# com = np.random.choice(['剪刀','石头','布'])
# print(com)
# xm = input('请输入你的选择（石头，剪刀，布）：')
# if xm == com:
#     print('平局')
# elif xm == '石头' and com == '石头':
#     print('你赢了')
# elif xm == '石头' and com == '布':
#     print('你输了')
# else:
#     print('输入无效')



#输入一个5位数，判断是否为回文数（12321）
# num = input('请输入一个任意数：')
# if num == num[::-1]:
#     print ('这是一个回文数')
# else:
#     print ('这不是一个回文数')




#音乐播放
# import time
# import pygame
# file = r'E:\KuGou\王一博、肖战 - 沧海一声笑 (2019天天向上11周年生日庆典现场).mp3'
# pygame.mixer.init()
# print('播放音乐1')
# track = pygame.mixer.music.load(file)
# pygame.mixer.music.play()
# time.sleep(10)
# pygame.mixer.music.stop()




#1~100相加
# s = 0
# for n in range(1,101):
#     s += n 
# print(s)





#100以内奇数与奇数相加，偶数与偶数相加
# s = 0
# z = 0
# for n in range(101):
#     if n % 2 == 0:
#         s += n  
#     else:
#         z += n    
# print(s)
# print(z)




#测试电脑性能
# import time
# start = time.time()
# sum_ = 0
# for i in range (1000000):
#     sum_ += i
# end = time.time()
# print(end - start)




#9x9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d' %(j,i,i*j),end='\t')
#     print(end='\n')

#9x9反过来
# for i in range(9,0,-1):
#     for j in range(i,0,-1):
#         print('%d*%d=%d' %(j,i,i*j),end='\t')
#     print(end='\n')


#素数（for与else结构）
# n = int(input("请输入一个正整数n:"))
# if n < 2:           #判断是否大于1的整数，且1不是素数
#     print("%d不是素数！"%n)
# else:
#     for i in range(2,n):
#         if n % i == 0:    #判断2——i是否有能被整除
#             print("%d不是素数！"%n)
#             break
#     else:
#         print("%d是素数！"%n)



#while 循环经常用于死循环
#当条件成立的时候执行执行体
# i = 0
# while i < 10:
#     print('xxx')
#     i += 1


#遍历j
# i = 0
# j = 'abcdefg'
# while i < len(j):
#     print(j[i])
#     i += 1



#让用户一直输入数字，然后让这些数字求和
# i = 0
# sum_ = 0
# i = input('>>')
# while i != '=':
#     sum_ += int(i)
#     i = input('>>')
# print(sum_)




