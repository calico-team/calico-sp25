all: blocks blocks_fullTree blocks_y blocks_code.cpp

blocks: blocks.cpp debug.h
	g++ -std=c++11 blocks.cpp -o blocks

blocks_fullTree: blocks_fullTree.cpp
	g++ -std=c++11 blocks_fullTree.cpp -o blocks_fullTree

blocks_y: blocks_y.cpp debug.h
	g++ -std=c++11 blocks_y.cpp -o blocks_y

blocks_code.cpp: blocks.cpp
	grep -v debug blocks.cpp >blocks_code.cpp
