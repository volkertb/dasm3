import sys
import mz
import dasm3

# Writes the instructions retrieved from the first 64K (if available) of data following
# the executable header.  The segment may be specified, but the initial offset is presumed
# to be zero.
def dump_first_code_segment (src_pn, segment=0):
    hdr = mz.MzHeader (src_pn); 
    src_fp = file (src_pn, 'rb')
    ccs = hdr.calc_code_start ()
    print ccs
    src_fp.seek (ccs)

    d = dasm3.Disassembler ()
    seg_len = min (1 << 16, hdr.calc_length () - hdr.calc_code_start ())
    block = 0
    for i in d.disassemble (src_fp.read (seg_len), segment=segment, trap=1, quiet=0):
        print i
        if (i.addr.offset >> 12) != block:
            block = i.addr.offset >> 12
            print 'Processed address ' + str (i.addr)

dump_first_code_segment (sys.argv[1])
