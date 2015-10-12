#coding:utf-8
import cv2.cv as cv

colorw = (255,255,255)
colorb = (0,0,0)
image = 1

# 画白色格子,左上角坐标
def drawCell(x0,y0):
	rect_start = (x0,y0) 
	x1 = x0+100
	y1 = y0+100
	rect_end = (x1,y1)
	cv.Rectangle(image, rect_start, rect_end, colorw, -1, 0)

# 画黑色直线,起始点坐标
def drawLine(x0,y0,x1,y1):
	cv.Line(image, (x0,y0), (x1,y1), colorb, 1, 8)

# 画棋盘,给定画的条数
def init(width,height):
	cv.Rectangle(image, (500,0), (700,600), colorw, -1, 0)
	for i in range(width):
		drawLine(i*100,0,i*100,600)
	for i in range(height):
		drawLine(0,i*100,1200,i*100)
# 画变化图像
def drawTwo(p,a):
	global image
	width = 1200
	height = 600
	no_of_bits = 8
	channels = 3
	image = cv.CreateImage((width,height), no_of_bits, channels)
	win_name = "hebb"
	cv.NamedWindow("hebb",cv.CV_WINDOW_AUTOSIZE)
	cv.ShowImage(win_name, image)
	
	
	for i in range(30):
		if p[i] == -1:
			x = i % 5
			y = (i - x) / 5
			drawCell(x*100,y*100)
	
	for i in range(30):
		if a[i] == -1:
			x = i % 5
			y = (i - x) / 5
			drawCell(700+x*100,y*100)
	
	init(13,7)
	
	cv.ShowImage(win_name, image)
	cv.WaitKey()