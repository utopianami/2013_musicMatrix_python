# -*- coding: UTF-8 -*-
from music_db import *
import random


#engine
class engine_pattern:

	#DB에서 '음악'을 기준으로 메트릭스를 구성한다.
	# 1행은 : 1번노래[들은사람], 2행은 : 2번노래[들은사람]
	def music_matrixGet(self, DB):
		self.music_matrix = {}
		for music in DB:
			self.music_matrix.update({DB[music]['info']['val']:DB[music]['people']})
		print self.music_matrix

	#DB에서 '사람'을 기준으로 메트릭스를 구성한다.
	# 1행은 : 1번사람[들은노래], 2행은 : 2번사람[들은노래]	
	def people_matrixGet(self):
		self.people_matrix = {}

		for music in self.music_matrix:
			for people in self.music_matrix[music]:
				if people in self.people_matrix:
					self.people_matrix[people].append(music)
				else:					
					self.people_matrix.update({people:[]})
					self.people_matrix[people].append(music)
		print self.people_matrix

	#행렬 곱
	#인자값에 넣는 따라 곡간의 패턴, 사람간의 패턴을 찾는다.
	def multi(self, var):
		self.result_matrix = {}
		self.music_pattern = {}
		self.people_pattern = {}
		self.count = 0

		if var == 'music':
			self.matrix = self.music_matrix
			self.music_pattern = self.result_matrix

		elif var == 'people':
			self.matrix = self.people_matrix
			self.people_pattern = self.result_matrix
		else:
			print 'error'

		for row in self.matrix:
			self.result_matrix.update({row:[]})
			for col in self.matrix:
				for val in self.matrix[row]:
					for val2 in self.matrix[col]:
						if val == val2:
							self.count += 1
				self.result_matrix[row].append(self.count)
				self.count = 0

		if var == 'music':
			print self.music_pattern
		elif var =='people':
			print self.people_pattern

class engine_recommend(engine_pattern):
	def choice_people(self, user, matrix):
		self.max_val = -1 #최고값 저장
		self.position = 0 #위치 저장
		self.position_list = []
		self.index = 0

		
		for val in matrix[user]:
			if (self.max_val == val) & (self.position != user):
				self.position_list.append(self.position)			
			elif (self.max_val < val) & (self.position != user) & (len(self.position_list)==0):
				self.position_list.append(self.position)
				self.max_val = val
			elif (self.max_val < val) & (len(self.position_list)!=0):
				self.position_list.pop()
				self.position_list.append(self.position)
				self.max_val = val
			self.position +=1

		#값이 동일한 값 _ random 추출
		self.index = random.randrange(0,len(self.position_list))
		print matrix[user]
		print ' %d 사용자와 유사한 사람은 %d이며, 공통 노래수는 %d' % (user, self.position_list[self.index], self.max_val)
		print '유사한 사람의 리스트', self.position_list


	def choice_music(self, user, matrix):
		print '나와 유사한 사람의 총 노래는', matrix[self.index]
		print '나의 노래는 ', matrix[user]
		self.recommend_music = []
		self.final_song = -1

		for val in matrix[self.index]:
			if val  not in matrix[user]:
				self.recommend_music.append(val)


		#듣지 않은 곡중에서 랜덤하게 추천
		self.num = random.randrange(0, len(self.recommend_music))
		self.final_song = self.recommend_music[self.num]
		print '추천하는 곡은 %d' % self.final_song


		#범위에 아무것도 없을때 처리


#create class
sample = engine_pattern()
sample2 = engine_recommend()


#test engine_pattern

sample.music_matrixGet(DB)
sample.people_matrixGet()
sample.multi('music')
sample.multi('people')

#test engine_recommend
sample2.choice_people(0, sample.people_pattern)
sample2.choice_music(0, sample.people_matrix)













