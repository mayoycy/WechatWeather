from PIL import Image, ImageDraw, ImageFont
from os import path
from matplotlib.font_manager import fontManager
import matplotlib as mpl
import matplotlib.pyplot as plt
import getWeather
import random

tongxue = ['重庆', '北京']
aiba = ['上海', '扬州', '杭州', '福州']
  
# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
font = ImageFont.truetype('wqy-zenhei.ttc', 44,index=0)
  
# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(image, text, font=font):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay) 
    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image)
    # text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)  #底部
    text_xy = ((rgba_image.size[0] - text_size_x)/2, (rgba_image.size[1] - text_size_y)/2) #中间
    # 设置文本颜色和透明度
    image_draw.text(text_xy, text, font=font, fill=(76, 234, 124, 180))
    # image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 255))
  
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)
  
    return image_with_text

def makepic1():
    tianqi = ''
    for city in tongxue:
        data = getWeather.get_weather(city)
        tianqi += city +': '+data['date']+' '+data['type']+'\n'+data['high']+' '+data['low']+' '+data['fengxiang']
        tianqi += '\n'
        tianqi += '\n'
    choice1 = random.randint(1, 10)
    pic1 = str(choice1) + '.png'
    im_before = Image.open(pic1)
    # im_before.show()  #打开图片
    im_after = add_text_to_image(im_before, tianqi)
    im_after.save('after1.png')

def makepic2():
    tianqi = ''
    for city in aiba:
        data = getWeather.get_weather(city)
        tianqi += city +': '+data['date']+' '+data['type']+'\n'+data['high']+' '+data['low']+' '+data['fengxiang']
        tianqi += '\n'
        tianqi += '\n'
    choice2 = random.randint(1, 10)
    pic2 = str(choice2) + '.png'
    im_before = Image.open(pic2)
    # im_before.show()  #打开图片
    im_after = add_text_to_image(im_before, tianqi)
    im_after.save('after2.png')

