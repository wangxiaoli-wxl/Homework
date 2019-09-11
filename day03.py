'''
在python中函数是一定有返回值的。如果你没有定义return，
则返回None，否则返回你的return值。
需要注意的是：一般只有在你需要继续使用函数返回的值
             的时候，你才定义return。

'''
#定义函数
'''
标识   函数名        参数可选
def  function_name([parms]):
    pass       执行体
    [return xxxx ]    返回
function_name([parms])
'''





#  def wdd(A):
#     res = 1
#     for i in range(1, A + 1):
#         res *= i
#     return res
# M = wdd(7)
# N = wdd(3)
# MN = wdd(4)
# print(M // N //MN)



#奇偶数
# def wdd(A):
#     if A % 2 == 0:
#         print('oushu')
#     else:
#         print('jishu')
# wdd(10)
# wdd(11)
# wdd(15)



#素数
# def wdd(A):
#     for i in range(2,A):
#         if A % i == 0:
#             print('bushisushu')
#             break
#     else:
#         print('sushu')
# wdd(7)
# wdd(12)



#账户密码
# def wdd(a,b):
#     if a == 'hhh' and b == '1234':
#         print('登陆成功')
#     else:
#         print('登陆失败')

# wdd('hhhh','2345')
# wdd('hhh','1234')        


#账户密码（验证码 ）
# import random
# def wdd(a,b):
#     y = random.randrange(1000,9999)
#     res = int(input('y是：%d >>'%y))
#     if res == y:
#         if a == 'hhh' and b == '1234':
#             print('登陆成功')
#         else:
#             print('登陆失败')
#     else:
#         print('y错误')

# wdd('hhh','1234') 




#账户密码（验证码  密码三次 ）
# import random
# count = 1
# def wdd():
#     global count
#     username = input('请输入账号：')
#     password = input('请输入密码：')
#     y = random.randrange(1000,9999)
#     res = int(input('y是：%d >>'%y))
#     if res == y:
#         if a == 'hhh' and b == '1234':
#             print('登陆成功')
#         else:
#             print('登陆失败')
#             if count != 3:
#                 count += 1
#                 wdd()
#             else:
#                 print('没机会了')
#     else:
#         print('y错误')

# wdd() 




#账户密码（验证码  密码三次 验证码由数字与字母组合[区分大小写]  验证码只能错5次
#      使用wxpy/互译无线/邮箱来实现类似于短信验证码功能）
'''
局部变量和全局变量
函数体内不可修改全局变量
so需要使用global 声明全局变量。
'''

"""

1. 模拟账号密码登录
2. 验证码生成
3. 试错(可有可无)
4. 调用外部包
   """
# import numpy as np

# ORIGINAL_USERNAME = 'admin'
# ORIGINAL_PASSWORD = '123'
# VERIFY_COUNT = 1
# def Check(username, password):
#     # 当函数体内需要改变外部变量的时候我们才需要global,但是统一起见都写上
#     global ORIGINAL_USERNAME, ORIGINAL_PASSWORD,VERIFY_COUNT
#     if username == ORIGINAL_USERNAME and password == ORIGINAL_PASSWORD:
#         print('登录成功')
#     else:
#         print('登录失败')
#         if VERIFY_COUNT != 3:
#             VERIFY_COUNT += 1
#             Login()
#         else:
#             print('账号密码输入次数达到上限，请24小时后再试！')
        
        
# def Login():
#     username = input('请输入账号:>>')
#     password = input('请输入密码:>>')
#     V_res = Verify()
#     if V_res == True:
#         Check(username, password)
#     else:
#         for _ in range(4):
#             V_res = Verify()
#             if V_res:
#                 Check(username, password)
#                 break
#         else:
#             print('验证码错误次数过多,怀疑你是一个机器人.')

# def Verify():
#     """
#     生成验证码
#     """
#     word = ""
#     word_list = [
#         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r',
#         't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
#         'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
#     ]
#     for _ in range(4):
#         word += np.random.choice(word_list)
#     user_word = input('请输入验证码%s:>>'%word)
#     if user_word == word:
#         return True
#     else:
#         return False

# def API():
#     pass

# def Start():
#     Login()

# if __name__ == "__main__":
#     Start()





# def yzm():
#     code = '' 
#     for i in range(0, 4):
#         num = str(random.randint(0, 9))
#         zm = chr(random.randint(65, 90))
#         lst = [num, zm]
#         ret = random.choice(lst)
#         code = ''.join([code, ret])  
#     print(code)
# yzm()



# m = 7
# n = 3
# M = 1
# N = 1
# mn = 1
# for i in range(1,M + 1):
#     m *= i
# for i in range(1,N + 1):
#     n *= i
# for i in range(1,(M - N) + 1):
#     mn *= i

# print(m / n / mn)




将一个文件引入另一个文件时：只需要保证一件事情，两个文件必须要在同一个文件夹内，
不同文件夹需要使用sys进行路径告知。详情--请百度