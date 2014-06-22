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
		"""
		コンストラクタ
		@parm surface	表層形
		@parm base	基本形
		@parm pos	品詞
		@parm pos1	品詞細分類1
		"""
		self.surface = surface
		self.base = base
		if base == "*":
			self.base = surface
		self.pos = pos
		self.pos1 = pos1

	def __str__(self):
		"""
		インスタンスを文字列でキャストしたときの動作
		@return	"surface base pos pos1"
		"""
		return self.surface+" "+self.base+" "+self.pos+" "+self.pos1

	def posIs(self, pos_str):
		"""
		品詞がpos_strであるかどうか
		@parm	pos_str 確かめたい品詞
		@return	一致していればTrue
		"""
		return pos_str==self.pos

	def pos1Is(self, pos1_str):
		"""
		品詞細分類がpos1_strであるかどうか
		@parm pos1_str	確かめたい品詞細分類
		@return	一致していればTrue
		"""
		return pos1_str==self.pos1

	def isNoun(self):
		"""
		品詞が名詞であるかどうか
		@return	名詞ならばTrue
		"""
		return self.pos == "名詞"

	def isIndipendent(self):
		"""
		自立語かどうか
		自立語はMecabの出力でいうと第一品詞が助詞か助動詞か記号でなく、かつ第二品詞が「非自立」でないもの
		"https://twitter.com/torotoki/status/225870997021130752"
		@return	自立語ならばTrue
		"""
		return not self.pos == "助詞" and not self.pos == "助動詞" and not self.pos == "記号"\
				and not self.pos1 == "非自立語"

class Chunk:
	"""
	文節を表すクラス
	"""
	def __init__(self, morphs, dst, srcs, ID, head):
		"""
		コンストラクタ
		@parm	morphs	文節が含んでいる形態素(Morph)のリスト
		@parm	dst	この文節が係っている文節のID
		@parm	srcs	この文節に係っている文節のIDのリスト
		@parm	ID	文ごとにユニークなID
		@parm	head	主辞の位置(morphs[head]が主辞)
		"""
		self.morphs = morphs
		self.dst = dst
		self.srcs = srcs
		self.ID = ID
		self.head = head

	def __str__(self):
		"""
		インスタンスを文字列でキャストしたときの動作
		@return	文節が持つ全ての形態素の表層形を接続した文字列
		"""
		return "".join([morph.surface for morph in self.morphs])

	def inPos(self, pos_str):
		"""
		文節が持つ形態素の中にたかだか1つでもpos_strの品詞があるかどうか
		@parm	pos_str	確かめたい品詞
		@return	品詞が存在すればTrue
		"""
		for morph in self.morphs:
			if morph.posIs(pos_str):
				return True
		return False

	def inPos1(self, pos1_str):
		"""
		文節が持つ形態素の中にたかだか1つでもpos1_strの品詞細分類があるかどうか
		@parm	pos_str	確かめたい品詞細分類
		@return	品詞細分類が存在すればTrue
		"""
		for morph in self.morphs:
			if morph.pos1Is(pos1_str):
				return True
		return False

	def withoutPos(self, pos_str):
		"""
		任意の品詞を除いた形態素で構成される文節(Chunk)を作る
		@parm	pos_str	除きたい品詞
		@return	pos_strを除いた新しい文節(Chunk)
		"""
		new_morphs=[]
		for morph in self.morphs:
			if not morph.posIs(pos_str):
				new_morphs.append(morph)
		return Chunk(new_morphs, self.dst, self.srcs, self.ID, self.head)

	def getNP(self):
		"""
		名詞句を抜き出す
		@return	名詞句を構成する形態素(Morph)のリスト
		"""
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
	"""
	ラティス形式のCaboChaの出力ファイルからリスト構造(list in list)を作る
	text = 文(sent)を要素としたリスト
	sent = 文節(Chunk)を要素としたリスト
	@return text
	"""
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
