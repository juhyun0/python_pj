from tkinter import*
import time
import random

WIDTH=800
HEIGHT=400

class Ball:
	def __init__(self,canvas,color,size,x,y,xspeed,yspeed):
		self.canvas=canvas	#캔버스 객체
		self.color=color
		self.size=size
		self.x=x
		self.y=y
		self.xspeed=xspeed
		self.yspeed=yspeed
		self.id=canvas.create_oval(x,y,x+size,y+size,fill=color)
	def move(self):	#ball을 이동시키는 함수
		self.canvas.move(self.id,self.xspeed,self.yspeed)
		(x1,y1,x2,y2)=self.canvas.coords(self.id)	#공의 현재 위치
		(self.x,self.y)=(x1,y1)
		if x1<=0 or x2>=WIDTH:	#공의 x좌표가 음수이거나, x좌표가 오른쪽 경계 넘으면
			self.xspeed=-self.xspeed	#속도부호 반전
		if y1<=0 or y2>=HEIGHT:
			self.yspeed=-self.yspeed

#생성된 포탄을 저장하는 리스트
bullets=[]

#이벤트를 처리하는 함수
def fire(event):
	bullets.append(Ball(canvas,"red",10,150,250,10,0))	

window=Tk()
canvas=Canvas(window,width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind("<Button-1>",fire)

spaceship=Ball(canvas,"green",100,100,200,0,0)
enemy=Ball(canvas,"red",100,500,200,0,5)

while True:
	for bullet in bullets:
		bullet.move()
		#포탄이 화면 벗어나면 삭제
		if(bullet.x+bullet.size)>=WIDTH:
			canvas.delete(bullet.id)
			bullets.remove(bullet)
	enemy.move()
	window.update()
	time.sleep(0.03)
