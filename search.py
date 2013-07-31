# -*- coding: UTF-8 -*-

from Tkinter import *

#header
app = Tk()
app.title = ("I konw your thinking")
app.geometry('300x450+500+100')


#function

def insertName_click():
	pass

def getInfo_click():
	pass


titleLabel = Label(app, text = '오늘은 무슨 곡을 들을까?', height=2).pack()
nameLabel = Label(app, text = '이름', width = 4, height=2).pack(side = 'left')
nameEntry = Entry(app).pack(side = 'left')
nameButton = Button(app, text = '입력', width = 7, command = insertName_click).pack(side ='left')


nameLabel = Label(app, text = '노', width = 4, height=2).pack(side = 'left')
nameEntry = Entry(app).pack(side = 'left')
getInfoButton = Button(app, text = '입력', width = 5, command = getInfo_click).pack(side ='bottom')





app.mainloop()




'''
#labe = 환영 / 도움말 / 숫자입력 / 상황판/ 메모
Label(app, text='Baseballgame에 오신 것을 환영합니다.', height=2).pack()
Label(app, textvariable = message).pack(side = 'bottom')
#Label(app, textvariable = message1).pack(side='left')


#버튼생성
b1 = Button(app, text="도움말", width = 7, command = help_click).pack()
b2 = Button(app, text="Playball", width = 7, command = playball_click).pack()
b3 = Button(app, text='New Game', width = 45).pack(side = 'bottom')

#숫자입력 & 상황판 & memo
number_entry = Entry(app)
number_entry.pack()
view_text = Text(app, width = 25, height = 30).pack(side='left')
memo_text = Text(app, width = 25, height = 30).pack(side='right')'''
