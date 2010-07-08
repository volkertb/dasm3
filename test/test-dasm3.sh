
export PYTHONPATH=..

# we keep binaries in the DOSBOX directory,
# for easier testing with the DOSBOX emulator
# we disassemble the prefab RANDOM.COM. For
# dosbox debug.exe compliancy, we pass 076B:0100
# as starting address
./test.py DOSBOX/RANDOM.COM 076B:0100 > test-debug-exe.out

# with our disassembly in test-debug-exe.out,
# we can compare it with the output from an
# actual DEBUG.EXE, stored in DOSBOX/RANDOM.DOT
# 'all' parameter means that tdiff.py shall not
# stop upon the first difference it encounters
./tdiff.py all DOSBOX/RANDOM.DOT test-debug-exe.out > good.tdiff 2> bad.tdiff

# bad should be much smaller than good
# wc *.tdiff

# make sure that dasm3.py's disassembly is different
# from DEBUG.EXE's only for crappy "unundocumented" 
# instructions
./okaytdiff.py < bad.tdiff

# If everything is right, no output is produced


