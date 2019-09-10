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









