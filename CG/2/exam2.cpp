/***
@InnerAc
题目要求：
(1) 采用Bresenham离线法绘出起点(1,3),终点为(9,18)的直线段。
(2) 用中点画圆法生成圆心在(3,-2)，半径为12的上半个半圆。
*/
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;
void draw(int x, int y){
	printf("(%d,%d) ",x,y);
}
void bresenham(int x1, int y1, int x2, int y2){
	double k = (double)(y1 - y2)/(double)(x1 - x2);
	double e = 0.0;
	double dx = x1,dy = y1;
	int x = x1, y = y1;
	while(x <= x2){
		e = dy - y;
		y = dy;
		if(e > 0.5){
			y++;
		}
		draw(x,y);
		x++;
		dy += k;
	}
}

double getY(int x,int r){
	return sqrt(r*r - x*x);
}

void pointCricle(int x, int y, int r){
	int x2 = r * sqrt(2)/2;
	int x0 = 0;
	int y0 = r;
	double y1 = r;
	double e =0.0;
	while(x0 <= x2){
		draw(x0+x,y0+y);
		draw(y0+x,x0+y);
		draw(-x0+x,y0+y);
		draw(-y0+x,x0+y);
		cout<<endl;
		y1 = getY(x0,r);
		y0 = y1;
		e = y1 - y0;
		if(e > 0.5){
			y0++;
		}
		x0++;
	}
}

int main(){
	bresenham(1,3,9,18);
	pointCricle(3,-2,12);
	return 0;
}
/** bresenham Output
(1,3)
(2,5)
(3,7)
(4,9)
(5,11)
(6,13)
(7,15)
(8,17)
(9,19)
*/
/** pointCricle Output
(3,10)
(15,-2)
(3,10)
(-9,-2)
(4,10)
(15,-1)
(2,10)
(-9,-1)
(5,10)
(15,0)
(1,10)
(-9,0)
(6,10)
(15,1)
(0,10)
(-9,1)
(7,10)
(15,2)
(-1,10)
(-9,2)
(8,9)
(14,3)
(-2,9)
(-8,3)
(9,9)
(14,4)
(-3,9)
(-8,4)
(10,8)
(13,5)
(-4,8)
(-7,5)
(11,8)
(13,6)
(-5,8)
(-7,6)
*/
