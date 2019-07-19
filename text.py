from PIL import Image, ImageDraw, ImageFont
from os import path
from matplotlib.font_manager import fontManager
import matplotlib as mpl
import matplotlib.pyplot as plt
import getWeather
import random

tongxue = ['重庆', '北京']
aiba1 = ['上海', '扬州', '杭州']
aiba2 = ['无锡', '苏州', '福州']
  
# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
font = ImageFont.truetype('wqy-zenhei.ttc', 60, index=0)
  
# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(image, text, font=font):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay) 
    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image)
    text_xy = ((rgba_image.size[0] - text_size_x)/2, rgba_image.size[1] - text_size_y)  #底部
    # text_xy = ((rgba_image.size[0] - text_size_x)/2, (rgba_image.size[1] - text_size_y)/2) #中间
    # 设置文本颜色和透明度
    image_draw.text(text_xy, text, font=font, fill=(0, 255, 255, 255))
    # image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 255))
  
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)
  
    return image_with_text

def makepic(forwhom, output):
    tianqi = ''
    for city in forwhom:
        data = getWeather.get_weather(city)
        tianqi += '\n'
        tianqi += city +': '+data['date']+' '+data['type']+'\n'+data['high']+' '+data['low']+' '+data['fengxiang']
        tianqi += '\n'
    choice = random.randint(1, 30)
    pic = str(choice) + '.png'
    im_before = Image.open(pic)
    # im_before.show()  #打开图片
    im_after = add_text_to_image(im_before, tianqi)
    im_after.save(output)

