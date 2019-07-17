import itchat
import datetime
import time
import text

tongxue = ['重庆', '北京']
aiba = ['上海', '扬州', '杭州', '福州']


def send(picture, qun):
    qunfa = itchat.search_chatrooms(name=qun)
    username = qunfa[0]['UserName']
    itchat.send_image(picture, toUserName=username)
    
if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True) # 二维码登陆，保持登陆
    #while True:
        #time_now = datetime.datetime.now()
        #if time_now.hour == 19 and time_now.minute == 43: 
    text.makepic1()
    send('after1.png','学术交流群')
    text.makepic2()
    send('after2.png','学习+偶像+健身+方舟')
    #        time.sleep(60)
     #   else:
      #      print('waiting')
       #     time.sleep(60)
            
