# -*- coding: UTF-8 -*-

DB	 = { 
'this love' : {
	'info' : { 'val' : 1, 'count' : 3, 'singer' : 'maroon5' },
	'people' : [1,2,5,6]},

'big girl' : {
	'info' : { 'val' : 2, 'count' : 3, 'singer' : 'mika' },
	'people' : [1,2,4,6]},

'moai' : {
	'info' : { 'val' : 3, 'count' : 2, 'singer' : 'seotaiji' },
	'people' : [3,4,6]},

'gentleman' : {
	'info' : { 'val' : 4, 'count' : 4, 'singer' : 'psy' },
	'people' : [2,3,4,5,6]},

'trouble' : {
	'info' : { 'val' : 5, 'count' : 3, 'singer' : 'coldplay' },
	'people' : [1,4,5,6]},

}


#engine
class engine_songPattern:
	def music_matrixGet(self, DB):
		self.music_matrix = {}
		for music in DB:
			self.music_matrix.update({DB[music]['info']['val']:DB[music]['people']})


		print self.music_matrix

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

	def multi(self, var):
		if var == 'music':
			self.matrix = self.music_matrix
		elif var == 'people':
			self.matrix = self.people_matrix
		else:
			print 'error'

		self.result_matrix = {}
		self.count = 0

		for row in self.matrix:
			self.result_matrix.update({row:[]})
			for col in self.matrix:
				for val in self.matrix[row]:
					for val2 in self.matrix[col]:
						if val == val2:
							self.count += 1
				self.result_matrix[row].append(self.count)
				self.count = 0

		print self.result_matrix


test = engine_songPattern()
test.music_matrixGet(DB)
test.people_matrixGet()
test.multi('music')
test.multi('people')

