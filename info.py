#coding:utf-8
#导入需要使用的相关模块
import itchat
import re
import os
import jieba
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
import PIL.Image as Image
from os import path
import math
from scipy.misc import imread   

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

#登录方法，会弹出登录二维码，用微信扫描登录
itchat.auto_login()     

#关于所有微信还有的资料信息都封装在这个方法里
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

#获取好友性别信息
male = female = other = 0

#遍历好友信息
for i in friends[1:]:
    #按照微信资料上的信息规则，男1，女2，其他3
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female +=1
    else:
        other +=1

total = len(friends[1:])

print('男生好友：%.2f%%' % (float(male)/total*100) + '\n' +
'女生好友：%.2f%%' % (float(female)/total*100) + '\n' +
'不明性别好友：%.2f%%' % (float(other)/total*100) + '\n' )


#获取好友签名信息
siglist = []

#遍历好友信息
for i in friends:
    #过滤信息
    signature = i['Signature'].strip().replace('span','').replace('class','').replace('emoji','')
    rep = re.compile('1f\d+\w*|[<>/=]')
    signature = rep.sub('',signature)
    siglist.append(signature)

#所有签名信息封装在text中
text = ''.join(siglist)

#写入本地文件
textfile = open('info.txt','w')
textfile.write(text)

print "finish"