# dasm3
dasm3 is an 8086 disassembler in python

Exported from https://code.google.com/archive/p/dasm3/, originally hosted there by transistorski, who also wrote [this project's wiki](../../wiki).

This README was mostly copied from there as well.

## Features

* simple python code (ca. 400 lines)
* comes with its own `.EXE` loader, can handle segments
* disassembly output is like `DEBUG.EXE`'s, but can be adapted to other disassembly formats easily

## Limitations, requirements

* [dasm3.py](./dasm3.py) is Unix-chauvinistic in that the shell scripts for testing are made for Unix; actual disassembly should work on Microsoft Windows, too
* for completely duplicating the tests on Unix, you need DOSBOX (https://www.dosbox.com/) or a similar emulator for running `DEBUG.EXE` (you can run the tests against a pre-fab trusted file without, however)
* no support for 8087 floating point instructions (0xD8-0xDF opcodes are invalid)
* the discussion of how the code works requires basic understanding of the 8086 registers and assembly language

## Credits

Michael Heyeck is the original author of [dasm3.py](./dasm3.py). You can find important documentation for [dasm3.py](./dasm3.py) in the original author's blog posts, at http://www.mlsite.net/blog/?s=disassembler. **HOWEVER**, there are minor differences:
* slightly modified opcode table for `DEBUG.EXE` compliancy
* slightly modified rendering of disassembly for `DEBUG.EXE` compliancy
* the demo discussed here: http://www.mlsite.net/blog/?p=60 does not accept an output filename, we dump to `stdout`

## Using dasm3

Explained in section "Demo" in the original author's article: http://www.mlsite.net/blog/?p=60

## How dasm3 works

Best enjoyed in the order listed:

* Opcode table: http://www.mlsite.net/blog/?p=57 and [UnderstandingTheOpcodeTable](../../wiki/UnderstandingTheOpcodeTable)
* A brief introduction, includes discussion of the .EXE header interpreter `mz.py`: http://www.mlsite.net/blog/?p=55
* A good discussion of the `.EXE` header format can be found here: http://www.nondot.org/sabre/os/files/Executables/EXE.txt
* [MimickingDebugExe](../../wiki/MimickingDebugExe) and http://www.mlsite.net/blog/?p=58
* [UnundocumentedOpcodeBlues](../../wiki/UnundocumentedOpcodeBlues)

## Tests

[MakingSureThatDasm3Works](../../wiki/MakingSureThatDasm3Works) -- this section discusses the test of [dasm3.py](./dasm3.py) against a file of random bytes, only mentioned in http://www.mlsite.net/blog/?p=60

## Some 8086 links for inclined parties

* learn 8086 assembly: http://www.xs4all.nl/~smit/asm01001.htm
* historical background (makeshift solutions are IMMORTAL): http://www.pcworld.com/article/146957/birth_of_a_standard_the_intel_8086_microprocessor.html
* Michael Heyeck datamining "duplicate" or "shorter" instructions: http://www.mlsite.net/blog/?p=76 and http://www.mlsite.net/blog/?p=83
