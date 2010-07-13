#!/usr/bin/python

import sys

# read in 'bad.tdiff'
lines_l = sys.__stdin__.readlines ()

for iter in lines_l:
	qiter = iter.strip ()
	if qiter:
		qiter_l = qiter.split ()
		invalid = qiter_l[2] == '???'
		if invalid:
			continue # this is okay, "category 1"
		elif qiter_l[2] == 'JMP':
			far = qiter_l[3] == 'FAR'
			if far and qiter_l[4] in "AX CX DX BX SP BP SI DI AH AL BH BL CH CL DH DL".split ():
				continue # this is okay
			else:
				# find out whether we are facing a CALL/JMP FAR INDIRECTION instruction 
				code = int (qiter_l[1], 16) # two-byte instructions remain
				opcode = code / 0x100		# insulate opcode
				modrmbyte = code % 0x100        # insulate mod-r/m byte
				mode = modrmbyte / 0x40
				instruction = (modrmbyte - mode * 0x40) / 8 # isolate the r/m bits, value enumerates instruction
				if opcode in [	0xFF, 
						0xFE,
						0xC5,
						0xC4,
						0x8D ] and mode == 3 and instruction in [3, 5]:
					continue # this is okay
				else:
				# we have found a genuine problem, i.e. incompatibility/difference
				# with/from DEBUG.EXE
					print >> sys.__stderr__, qiter 
						
		else:
			# we have found a genuine problem, i.e. incompatibility/difference
			# with/from DEBUG.EXE
			print >> sys.__stderr__, qiter 
