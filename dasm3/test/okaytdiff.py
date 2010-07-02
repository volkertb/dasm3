
#! /usr/bin/python

import sys

lines_l = sys.__stdin__.readlines ()

for iter in lines_l:
	qiter = iter.strip ()
	if qiter:
		qiter_l = qiter.split ()
		invalid = qiter_l[2] == '???'
		if invalid:
			continue
		elif qiter_l[2] == 'JMP':
			far = qiter_l[3] == 'FAR'
			if far and qiter_l[4] in "AX CX DX BX SP BP SI DI AH AL BH BL CH CL DH DL".split ():
				continue
			else: 
				code = int (qiter_l[1], 16)
				codeh = code / 0x100
				codel = code % 0x100
				mode = codel / 0x40
				# instruction = codel / 8 - mode * 8
				print "%x, %x, %x, %x" % (codeh, codel, mode, instruction)
				if codeh in [	0xFF, 
						0xFE,
						0xC5,
						0xC4,
						0x8D ] and mode == 3 and instruction in [3, 5]:
					continue
				else:
					print >> sys.__stderr__, qiter 
						
		else:
			print >> sys.__stderr__, qiter 
