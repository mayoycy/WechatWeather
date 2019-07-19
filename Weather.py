import itchat
import datetime
import time
import text

# 城市可自行定制
tongxue = ['重庆', '北京']
aiba1 = ['上海', '扬州', '杭州']
aiba2 = ['无锡', '苏州', '福州']
deguo = ['北京', '天津', '上海']


def send(picture, qun):
    qunfa = itchat.search_chatrooms(name=qun)
    username = qunfa[0]['UserName']
    itchat.send_image(picture, toUserName=username)
    
if __name__ == '__main__':
    #itchat.auto_login(enableCmdQR=2, hotReload=True) # 二维码登陆，保持登陆
    #while True:
        #time_now = datetime.datetime.now()
        #if time_now.hour == 19 and time_now.minute == 43:

    # 根据城市列表抓取天气数据, 并制成图片
    text.makepic(tongxue, 'after1.png')
    text.makepic(aiba1, 'after2.png')
    text.makepic(aiba2, 'after3.png')
    text.makepic(deguo, 'after4.png')
    # 发送指定图片到指定群聊
    #send('after1.png','学术交流群')
    #send('after2.png','学习+偶像+健身+方舟')
    #send('after3.png','学习+偶像+健身+方舟')
    #send('after4.png','18cmClub')
    #        time.sleep(60)
     #   else:
      #      print('waiting')
       #     time.sleep(60)
            
