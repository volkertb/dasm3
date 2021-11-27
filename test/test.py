#! /usr/bin/python

import sys
import os
sys.path.append(os.path.join('..','..'))
import dasm3

def dump_com_file (src_pn, segment, offset):
   src_fp = open (src_pn, 'rb')
   # dst_fp     = file(dst_pn, 'wb')
   dst_fp = sys.__stdout__ 
   d          = dasm3.Disassembler()
   # block      = 0
   for i in d.disassemble(src_fp.read(), segment, offset, trap=0, quiet=0):
       dst_fp.write(str(i)+'\n')
       # if ((i.addr.offset >> 12) != block):
           # block = i.addr.offset >> 12
           # print 'Processed address ' + str(i.addr)

if __name__ == '__main__':
    start = sys.argv[2].split (':')
    seg = int(start[0], 16) 
    off = int(start[1], 16)
    dump_com_file(sys.argv[1], seg, off)
