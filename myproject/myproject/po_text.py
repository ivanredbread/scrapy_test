# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 16:46:39 2017

@author: tedoreve
"""

from PIL import Image,ImageDraw,ImageFont  
ttfont = ImageFont.truetype("msyh.ttc",20) #这里我之前使用Arial.ttf时不能打出中文，用华文细黑就可以  
im = Image.open("drrr.jpg")  
draw = ImageDraw.Draw(im)  
draw.text((100,100),u'韩寒', fill=(106,126,164),font=ttfont)  
#draw.text((40,40),('杨利伟','utf-8'), fill=(0,0,0),font=ttfont)  
im.show()  
