# Copyright 2009 Michael Heyeck
# This file is part of dasm3.py.
#
# dasm3.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# 
# dasm3.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with dasm3.py.  If not, see <http://www.gnu.org/licenses/>.

import sys
from . import mz
from . import dasm3

# Writes the instructions retrieved from the first 64K (if available) of data following
# the executable header.  The segment may be specified, but the initial offset is presumed
# to be zero.
def dump_first_code_segment (src_pn, segment=0):
    hdr = mz.MzHeader (src_pn); 
    src_fp = file (src_pn, 'rb')
    ccs = hdr.calc_code_start ()
    print(ccs)
    src_fp.seek (ccs)

    d = dasm3.Disassembler ()
    seg_len = min (1 << 16, hdr.calc_length () - hdr.calc_code_start ())
    block = 0
    for i in d.disassemble (src_fp.read (seg_len), segment=segment, trap=1, quiet=0):
        print(i)
        if (i.addr.offset >> 12) != block:
            block = i.addr.offset >> 12
            print('Processed address ' + str (i.addr))

dump_first_code_segment (sys.argv[1])
