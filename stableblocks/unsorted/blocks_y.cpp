#include <algorithm>
#include <iostream>
#include <vector>

struct Corner
{
    // Problem implies that y-Axis is going up with
    // floor on the bottom.
    int x, y;
};

// Sort corners from top to bottom, left to right.
bool operator<(const Corner &a, const Corner &b)
{
    if (a.y > b.y) {
	return true;
    }
    if (a.y < b.y) {
	return false;
    }
    return a.x < b.x;
}

struct Block
{
    Corner lowerLeft;
    Corner upperRight;

    Corner UpperLeft() const { return { lowerLeft.x, upperRight. y }; }

    // Note that we only need to know the x-coordinate of the center of
    // mass which is given by
    // (m_0 * x_0 + ... + m_{n-1} * x_{n-1}) / (m_0 + ... + m_{n-1})
    //
    // where x_i is the x-coordinate of the center of mass of a block.
    //
    // We accumulate the denominator in totalMass and the numerator
    // in totalTorque for the block and all blocks connected to it from
    // above.

    double totalMass = 0;
    double totalTorque = 0;

    double totalMassY = 0;
};

#include "debug.h"

// {0, 1, ..., n - 1}
std::vector<int> indices(const int n)
{
    std::vector<int> result(n);
    for (int i = 0; i < n; i++) {
	result[i] = i;
    }
    return result;
}

bool is_stable(std::vector<Block> &blocks)
{
    // We want to process the blocks from top to bottom, left to
    // to right (by their lower left corner).
    std::sort(blocks.begin(), blocks.end(),
	      [](const Block &a, const Block &b) {
		  return a.lowerLeft < b.lowerLeft; });

    // To quickly look-up the block that this block rests on, make
    // an index sorted by upper left corner.
    std::vector<int> sortedByUpperLeft = indices(blocks.size());
    std::sort(
	sortedByUpperLeft.begin(),
	sortedByUpperLeft.end(),
	[&blocks](const int i, const int j) {
	    return blocks[i].UpperLeft() < blocks[j].UpperLeft(); });

    // Process each block in the order discussed above.
    for (Block &block : blocks) {
	if (block.lowerLeft.y == 0) {
	    // We reached the block resting on the floor. Stop.
	    break;
	}

	// Finally, add the contribution to mass and torque by the block itself.
	const int mass =
	    (block.upperRight.x - block.lowerLeft.x) *
	    (block.upperRight.y - block.lowerLeft.y);
	const double torque =
	    mass * (block.lowerLeft.x + block.upperRight.x) / 2.0;
	const double massY =
	    mass * (block.lowerLeft.y + block.upperRight.y) / 2.0;

	block.totalMass += mass;
	block.totalTorque += torque;
	block.totalMassY += massY;

	// Center of mass of the block and the blocks connected to it
	// from above.
	const double center_x = block.totalTorque / block.totalMass;
	const double center_y = block.totalMassY  / block.totalMass;

	// Find the block below this block.
	//
	// The upper edge has the same height as the lower edge of
	// this block.
	//
	// We have two cases based on whether the left edge is to
	// the left or right of the left edge of this block.

	const auto it = std::lower_bound(
	    sortedByUpperLeft.begin(),
	    sortedByUpperLeft.end(),
	    block.lowerLeft,
	    [ &blocks ](const int i, const Corner &c) {
		return blocks[i].UpperLeft() < c; });
	if (it == sortedByUpperLeft.begin()) {
	    // This block itself has a higher upper edge, so
	    // this cannot happen.
	    std::cerr << "Bad input (case 0)" << std::endl;
	    exit(1);
	}

	// Candidate for block below in case its left edge is left of
	// this block.
	Block *below = &blocks[*(it - 1)];
	if (below->upperRight.y != block.lowerLeft.y ||
	    below->upperRight.x < block.lowerLeft.x) {

            // Candidate did not work out.
	    if (it == sortedByUpperLeft.end()) {
		std::cerr << "Bad input (case 1)" << std::endl;
		exit(1);
	    }
	    // So it must be the other candidate.
	    below = &blocks[*it];
	    if (below->upperRight.y != block.lowerLeft.y) {
		std::cerr << "Bad input (case 2)" << std::endl;
		exit(1);
	    }
	}

	// Make sure that the center of mass of this block lies
	// between the left and right edge of the block below.
	if (center_x < below->lowerLeft.x ||
	    center_x > below->upperRight.x) {

	    debug_center(center_x, center_y, true);

	    return false;
	}

	debug_center(center_x, center_y, false);

	// Accumulate torque and mass.
	below->totalTorque += block.totalTorque;
	below->totalMassY += block.totalMassY;
	below->totalMass += block.totalMass;
    }

    return true;
}

int main()
{
    int numCases;
    std::cin >> numCases;

    for (int i = 0; i < numCases; i++) {
	debug_begin();

	int numBlocks;
	std::cin >> numBlocks;

	std::vector<Block> blocks;
	blocks.reserve(numBlocks);

	for (int b = 0; b < numBlocks; b++) {
	    Block block;
	    std::cin >> block.lowerLeft.x >> block.lowerLeft.y
		     >> block.upperRight.x >> block.upperRight.y;
	    debug_block(block);
	    blocks.push_back(std::move(block));
	}

	uint64_t totalMass = 0;
	for (const Block &block : blocks) {
	    if (!(block.lowerLeft.x < block.upperRight.x)) {
		std::cout << "Bad x" << std::endl;
		return 1;
	    }
	    if (!(block.lowerLeft.y < block.upperRight.y)) {
		std::cout << "Bad y" << std::endl;
		return 1;
	    }
	    if (block.lowerLeft.x < -10000) {
		std::cout << "Too negative x" << std::endl;
		return 1;
	    }
	    if (block.upperRight.x > 10000) {
		std::cout << "Too positive x" << std::endl;
		return 1;
	    }
	    const uint64_t mass =
		(block.upperRight.x - block.lowerLeft.x) *
		(block.upperRight.y - block.lowerLeft.y);
	    if (mass > 100000) {
		std::cout << "Too large individual mass" << std::endl;
		return 1;
	    }
	    totalMass += mass;
	    if (totalMass > 100000) {
		std::cout << "Too large total mass" << std::endl;
		return 1;
	    }
	}

	if (is_stable(blocks)) {
	    std::cout << "Stable" << std::endl;
	} else {
	    std::cout << "UNSTABLE" << std::endl;
	}
	debug_end();
    }
}
