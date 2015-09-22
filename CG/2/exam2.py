import cv2.cv as cv

color = (0,255,0)

def drawPoints(x,y):
	radius = 1
	circle_center = (250+x*10,250-y*10)
	cv.Circle(image, circle_center, radius, color)


width = 500
height = 500
no_of_bits = 8
channels = 3
image = cv.CreateImage((width,height), no_of_bits, channels)
win_name = "bresenham"
cv.NamedWindow("bresenham",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage(win_name, image)

bresenham = [[1,3],[2,5],[3,7],[4,9],[5,11],[6,13],[7,15],[8,17],[9,19]]
circle = [[3,10],[15,-2],[3,10],[-9,-2],[4,10],[15,-1],[2,10],[-9,-1],[5,10],[15,0],[1,10],[-9,0],[6,10],[15,1],[0,10],[-9,1],[7,10],[15,2],[-1,10],[-9,2],[8,9],[14,3],[-2,9],[-8,3],[9,9],[14,4],[-3,9],[-8,4],[10,8],[13,5],[-4,8],[-7,5],[11,8],[13,6],[-5,8],[-7,6]]
for [x,y] in bresenham:
# for [x,y] in circle:
	drawPoints(x,y)


cv.ShowImage(win_name, image)
cv.WaitKey()
