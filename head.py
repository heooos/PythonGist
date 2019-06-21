# -*- coding:utf-8 -*-
#导入相关模块
import itchat
import os
import PIL.Image as Image
from os import listdir
import math

#登录
itchat.auto_login(enableCmdQR=False)
#获取微信全部好友的信息
friends = itchat.get_friends(update=True)[0:]
#获取自己的用户名
user = friends[0]["UserName"]
#打印用户名
print(user)
#建立文件夹用来装好友的头像
os.mkdir(user)

num = 0
#遍历好友信息，将头像保存
for i in friends:
    img = itchat.get_head_img(userName=i["UserName"])
    fileImage = open(user + "/" + str(num) + ".jpg",'wb')
    fileImage.write(img)
    fileImage.close()
    num += 1

pics = listdir(user)
numPic = len(pics)
print(numPic)
eachsize = int(math.sqrt(float(640 * 640) / numPic))
print(eachsize)
numline = int(640 / eachsize)
toImage = Image.new('RGBA', (640, 640))
print(numline)

x = 0
y = 0

for i in pics:
    try:
        #打开图片
        img = Image.open(user + "/" + i)
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        #缩小图片
        img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
        #拼接图片
        toImage.paste(img, (x * eachsize, y * eachsize))
        x += 1
        if x == numline:
            x = 0
            y += 1

#保存拼接后的头像
toImage.save(user + ".BMP")
itchat.send_image(user + ".BMP", 'filehelper')