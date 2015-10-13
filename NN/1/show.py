#coding:utf-8
#InnerAc
import numpy as np
import cv2

colorw = (255,255,255)
colorb = (0,0,0)
image = 1

# 画白色格子,左上角坐标
def drawCell(x0,y0):
	rect_start = (x0,y0) 
	x1 = x0+100
	y1 = y0+100
	rect_end = (x1,y1)
	cv2.rectangle(image, rect_start, rect_end, colorw, -1)

# 画黑色直线,起始点坐标
def drawLine(x0,y0,x1,y1):
	cv2.line(image, (x0,y0), (x1,y1), colorb, 1, 8)

# 画棋盘,给定画的条数
def init(width,height):
	cv2.rectangle(image, (500,0), (700,600), colorw, -1)
	for i in range(width):
		drawLine(i*100,0,i*100,600)
	for i in range(height):
		drawLine(0,i*100,1200,i*100)
# 画变化图像
def drawTwo(p,a,name):
	global image
	width = 1200
	height = 600
	image = np.zeros((height,width), np.uint8)
	win_name = "hebb"
	cv2.namedWindow("hebb",cv2.CV_WINDOW_AUTOSIZE)
	cv2.imshow(win_name, image)
	
	
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
	
	cv2.imshow(win_name, image)
	cv2.imwrite(str(name)+".png",image)
	cv2.waitKey(0)