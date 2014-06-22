# !usr/bin/python
# coding:utf-8
"""
形態素や文節のクラスを定義している
"""
__author__  = "ryosuke <tmcit.miyazaki@gmail.com>"
__version__ = "1.00"
__date__    = "14/06/17"

import sys
from collections import defaultdict


class Morph:
	"""形態素を表すクラス"""
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		if base == "*":
			self.base = surface
		self.pos = pos
		self.pos1 = pos1
	def __str__(self):
		return self.surface+" "+self.base+" "+self.pos+" "+self.pos1
	def posIs(self, pos_str):
		return pos_str==self.pos
	def pos1Is(self, pos1_str):
		return pos1_str==self.pos1
	def isNoun(self):
		return self.pos == "名詞"
	def isIndipendent(self):
		"""自立語はMecabの出力でいうと第一品詞が助詞か助動詞か記号でなく、かつ第二品詞が「非自立」でないもの"""
		return not self.pos == "助詞" and not self.pos == "助動詞" and not self.pos == "記号"\
				and not self.pos1 == "非自立語"
class Chunk:
	def __init__(self, morphs, dst, srcs, ID, head):
		self.morphs = morphs
		self.dst = dst
		self.srcs = srcs
		self.ID = ID
		self.head = head
	def __str__(self):
		return "".join([morph.surface for morph in self.morphs])
	def inPos(self, pos_str):
		for morph in self.morphs:
			if morph.posIs(pos_str):
				return True
		return False
	def inPos1(self, pos1_str):
		for morph in self.morphs:
			if morph.pos1Is(pos1_str):
				return True
		return False
	def withoutPos(self, pos_str):
		new_morphs=[]
		for morph in self.morphs:
			if not morph.posIs(pos_str):
				new_morphs.append(morph)
		return Chunk(new_morphs, self.dst, self.srcs, self.ID, self.head)
	def getNP(self):
		pre_morph = self.morphs[0]
		nounFlag = False
		np_list = []
		for morph in self.morphs[1:]:
			if pre_morph.isNoun() and not nounFlag:
				np_list.append(pre_morph)
				nounFlag = True
			if pre_morph.isNoun() and morph.isNoun() and nounFlag:
				np_list.append(morph)
			elif nounFlag:
				break
			pre_morph = morph
		return np_list if len(np_list)>0 else None

def createChunksText(filename):
	text=[]
	sent=[]
	chunk = None
	srcs_dict = defaultdict(list)
	pre_line = ""
	for line in open(filename):
		line = line.strip()
		if pre_line=="EOS" and line == "EOS":
			continue
		if line.startswith("* "):
			if chunk is not None : sent.append(chunk)
			chunk = Chunk([], int(line.split()[2][:-1]), [], int(line.split()[1]), int(line.split()[3].split("/")[0]))
			srcs_dict[chunk.dst].append(chunk.ID)
			pre_line = line
			continue
		if line=="EOS":
			sent.append(chunk)
			for chunk in sent:
				chunk.srcs = srcs_dict[chunk.ID]
			text.append(sent)
			sent=[]
			chunk = None
			srcs_dict =defaultdict(list)
			pre_line = line
			continue
		chunk.morphs.append(Morph(line.split("\t")[0], line.split("\t")[1].split(",")[6],\
									line.split("\t")[1].split(",")[0], line.split("\t")[1].split(",")[1]))
		pre_line = line
	return text	

if __name__ == '__main__':
	text = createChunksText(sys.argv[1])
	for sent in text:
		for chunk in sent:
			print "ID:"+str(chunk.ID), "dst:"+str(chunk.dst), "srcs:"+str(chunk.srcs)
			for morph in chunk.morphs:
				print "\t", morph
