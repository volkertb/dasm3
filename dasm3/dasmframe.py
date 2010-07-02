import    sys
import    mz
import    dasm3

# Writes the instructions retrieved from the first 64K (if available) of data following
# the executable header.  The segment may be specified, but the initial offset is presumed
# to be zero.
def dump_first_code_segment(dst_pn, src_pn, segment=0):
    hdr = mz.MZ_Header(src_pn); 
    src_fp = file(src_pn, 'rb')
    ccs = hdr.calc_code_start()
    print ccs
    src_fp.seek(ccs)

    d          = dasm3.Disassembler()
    dst_fp     = file(dst_pn, 'wb')
    seg_len    = min(1<<16, hdr.calc_length()-hdr.calc_code_start())
    block      = 0
    for i in d.disassemble(src_fp.read(seg_len), segment=segment, trap=1, quiet=1):
        dst_fp.write(str(i)+'\n')
        if ((i.addr.offset >> 12) != block):
            block = i.addr.offset >> 12
            print 'Processed address ' + str(i.addr)

def dump_com_file (dst_pn, src_pn):
    src_fp = file (src_pn, 'rb')
    dst_fp     = file(dst_pn, 'wb')
    d          = dasm3.Disassembler()
    dst_fp     = file(dst_pn, 'wb')
    block      = 0
    for i in d.disassemble(src_fp.read(), segment=0, trap=1, quiet=0):
        dst_fp.write(str(i)+'\n')
        if ((i.addr.offset >> 12) != block):
            block = i.addr.offset >> 12
            print 'Processed address ' + str(i.addr)
	

dump_com_file ("dasmframe.out", sys.argv[1])
