# characterPicture
彩色字符画转换工具

	usage: trans.py [-h] [-i INPUTFILE] [-o OUTPUTFILE]
	usage: transPNG.py [-h] [-i INPUTFILE] [-o OUTPUTFILE]
	
	trans pic to charpic 
	
	
	optional arguments:
	  -h, --help     show this help message and exit
	  -i INPUTFILE   input pic file
	  -o OUTPUTFILE  output pic file,default output.html or output.png

说明
===========
* 将图片转换为彩色字符画
* -i 参数指定输入图片文件
* -o 参数指定字符画输出文件，默认为当前目录下的output.html或者output.png
* 为调整长宽合适的比例，高度取像素点的步长默认为2
* 使用分为两个版本，trans.py 脚本输出html文件   transPNG.py 脚本输出png图片   用法两者一样
* 输出png的脚本需要安装phantomjs 而且默认运行在windows，如果需要运行在linux上需要修改下脚本内容


example:

俺的老脸:

![我的老脸](https://github.com/mnpiozhang/characterPicture/blob/master/example/%E8%AF%81%E4%BB%B6%E7%85%A7%E5%AD%97%E7%AC%A6%E7%94%BB.jpg)

doge:

![doge](https://github.com/mnpiozhang/characterPicture/blob/master/example/dogecharpic.jpg)
