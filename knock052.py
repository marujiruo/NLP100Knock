# !usr/bin/python
# coding:utf-8
import sys

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

if __name__ == '__main__':
	text=[]
	sent=[]
	for line in open(sys.argv[1]):
		line = line.strip()
		if line.startswith("* "): continue
		if line=="EOS":
			text.append(sent)
			sent=[]
			continue
		sent.append(Morph(line.split("\t")[0], line.split("\t")[1].split(",")[6],\
			line.split("\t")[1].split(",")[0], line.split("\t")[1].split(",")[1]))
	for sent in text:
		for morph in sent:
			print morph.surface, morph.base, morph.pos, morph.pos1
