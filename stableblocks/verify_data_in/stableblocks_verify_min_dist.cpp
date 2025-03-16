// Check that the center of mass is not close to the left or right edge of the block below
// so that numerical issues could give the wrong result.

#include <algorithm>
#include <cmath>
#include <cstdint>
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

// {0, 1, ..., n - 1}
std::vector<int> indices(const int n)
{
    std::vector<int> result(n);
    for (int i = 0; i < n; i++) {
	result[i] = i;
    }
    return result;
}


bool is_center_of_mass_ambiguous(std::vector<Block> &blocks)
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

	if (!(fabs(center_x - below->lowerLeft.x) > 0.001 &&
	       fabs(center_x - below->upperRight.x) > 0.001)) {
	    return false;
	}

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
	int numBlocks;
	std::cin >> numBlocks;

	std::vector<Block> blocks;
	blocks.reserve(numBlocks);

	for (int b = 0; b < numBlocks; b++) {
	    Block block;
	    std::cin >> block.lowerLeft.x >> block.lowerLeft.y
		     >> block.upperRight.x >> block.upperRight.y;
	    blocks.push_back(std::move(block));
	}

	if (!is_center_of_mass_ambiguous(blocks)) {
	    std::cout << "CENTER OF MASS AMBIGUOUS " << i << std::endl;
	    return 1;
	}
    }
}
