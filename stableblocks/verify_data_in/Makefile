# Verifies that the input files data/secret/*.in are fulfilling the constraints.

# For further visually debugging, create svg files with:
# stableblocks_svg <../data/secret/main.in

all: stableblocks_svg main_verified bonus_verified

stableblocks_verify_full_binary_tree: stableblocks_verify_full_binary_tree.cpp
	g++ -std=c++17 -o stableblocks_verify_full_binary_tree stableblocks_verify_full_binary_tree.cpp

stableblocks_verify_forest: stableblocks_verify_forest.cpp
	g++ -std=c++17 -o stableblocks_verify_forest stableblocks_verify_forest.cpp

stableblocks_verify_min_dist: stableblocks_verify_min_dist.cpp
	g++ -std=c++17 -o stableblocks_verify_min_dist stableblocks_verify_min_dist.cpp

# 1. Check format, x and y coordinates and total mass.
# 2. Check boxes non-overlapping and topology.
main_verified: stableblocks_verify_full_binary_tree stableblocks_verify_min_dist
	python stableblocks_verify_constraints.py < ../data/secret/main.in
	./stableblocks_verify_full_binary_tree < ../data/secret/main.in
	./stableblocks_verify_min_dist < ../data/secret/main.in
	python stableblocks_verify_constraints.py < ../data/secret/main.in
	./stableblocks_verify_full_binary_tree < ../data/secret/main.in
	./stableblocks_verify_min_dist < ../data/secret/main.in

# Same
bonus_verified: stableblocks_verify_forest stableblocks_verify_min_dist
	python stableblocks_verify_constraints.py < ../data/secret/bonus.in
	./stableblocks_verify_forest < ../data/secret/bonus.in
	./stableblocks_verify_min_dist < ../data/secret/bonus.in
	python stableblocks_verify_constraints.py < ../data/secret/bonus.in
	./stableblocks_verify_forest < ../data/secret/bonus.in
	./stableblocks_verify_min_dist < ../data/secret/bonus.in

stableblocks_svg: stableblocks_svg.cpp
	g++ -std=c++17 -o stableblocks_svg stableblocks_svg.cpp

clean:
	rm -f stableblocks_verify_full_binary_tree stableblocks_verify_forest stableblocks_svg stableblocks_verify_min_dist
