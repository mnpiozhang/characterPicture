#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from PIL import Image
import argparse
import sys
import os

from selenium import webdriver


parser = argparse.ArgumentParser(description="trans pic to charpic")
parser.add_argument('-i',dest='inputfile',action='store',help='input pic file')
parser.add_argument('-o',dest='outputfile',action='store',help='output pic file,default output.html or output.png')
parser.add_argument('-hs',dest='height_step',action='store',help='read pic height step')
parser.add_argument('-ws',dest='width_step',action='store',help='read pic width  step')

args = parser.parse_args()

str1 = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")


def get_char(r, g, b):
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return str1[int(gray / 256.0 * len(str1))]

def create_PNG_file(htmlfile,outputPNGfile):
    driver=webdriver.PhantomJS(executable_path="phantomjs.exe")
    driver.get("file:///" + os.path.join(os.getcwd(),htmlfile))  
    driver.save_screenshot(outputPNGfile)
    driver.quit()


if __name__ == '__main__':
    if args.inputfile and os.path.exists(args.inputfile):
        #im = Image.open("HX2EJ9}812QI6RH@5YWRSXP.jpg")
        im = Image.open(args.inputfile)
    else:
        print "inputfilename is null or inputfilename is not exist.you can add -h arg get help info"
        sys.exit()
    try:
        if args.height_step:
            height_step = int(args.height_step)
        else:
            height_step = 2
        if args.width_step:
            width_step = int(args.width_step)
        else:
            width_step = 1
    except:
        print "height step or width step format error"
        sys.exit()

    w,h = im.size
    resulthtml = '<div style="font-size:0.48em;">'
    for j in range(0,h,height_step):
        for i in range(0,w,width_step):
            r,g,b = im.getpixel((i,j))
            txt = get_char(*im.getpixel((i,j)))
            pixchar = '<span style="color:rgb(%s, %s, %s);">%s</span>' %(r,g,b,txt)
            resulthtml = resulthtml + pixchar
        resulthtml = resulthtml + '<br>'
    resulthtml = resulthtml + '</div>'
    if args.outputfile:
        with open("tmpoutput.html",'w') as f:
            f.write(resulthtml)
        create_PNG_file("tmpoutput.html",args.outputfile)
    else:
        with open("tmpoutput.html",'w') as f:
            f.write(resulthtml)
        create_PNG_file('tmpoutput.html','output.png')