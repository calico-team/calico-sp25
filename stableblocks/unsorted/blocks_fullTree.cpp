#include <iostream>
#include <vector>

struct Corner
{
    // Problem implies that y-Axis is going up with
    // floor on the bottom.
    int x, y;
};

struct Block
{
    Corner lowerLeft;
    Corner upperRight;
};

// Result for a block and all blocks resting on it and
// all blocks resting on the blocks resting on it and so on...
struct StabilityResult
{
    // Are all blocks resting on this block and so on stable?
    bool isStable = true;

    // Note that we only need to know the x-coordinate of the center of
    // mass which is given by
    // (m_0 * x_0 + ... + m_{n-1} * x_{n-1}) / (m_0 + ... + m_{n-1})
    //
    // where x_i is the x-coordinate of the center of mass of a block.
    //
    // We accumulate the denominator in totalMass and the numerator
    // in totalTorque for the block and all blocks connected to it from
    // above.
    double totalMass = 0.0;
    double totalTorque = 0.0;
};

StabilityResult is_stable(
    const std::vector<Block> &blocks, const unsigned int i)
{
    StabilityResult totalResult;

    const Block &block = blocks[i];
    
    // Consider the two blocks resting on the current block.
    for (unsigned int j = 2 * i + 1; j <= 2 * i + 2; j++) {
	if (j < blocks.size()) {
	    const StabilityResult result = is_stable(blocks, j);

	    // Relevant center of mass.
	    const double center_x = result.totalTorque / result.totalMass;
	    if (center_x < block.lowerLeft.x ||
		center_x > block.upperRight.x) {
		// If it is not between the left and right edge of this
		// block, unstable.
		totalResult.isStable = false;
	    }
	    // Unstable if any blocks resting on blocks ... resting
	    // on this block was unstable.
	    totalResult.isStable &= result.isStable;

	    // Accumulate torque and mass.
	    totalResult.totalMass += result.totalMass;
	    totalResult.totalTorque += result.totalTorque;
	}
    }

    // Finally, add the contribution to mass and torque by the block itself.
    const int mass =
	(block.upperRight.x - block.lowerLeft.x) *
	(block.upperRight.y - block.lowerLeft.y);
    const double torque =
	mass * (block.lowerLeft.x + block.upperRight.x) / 2.0;
    totalResult.totalMass += mass;
    totalResult.totalTorque += torque;

    return totalResult;
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

	if (is_stable(blocks, 0).isStable) {
	    std::cout << "Stable" << std::endl;
	} else {
	    std::cout << "UNSTABLE" << std::endl;
	}
    }
}
