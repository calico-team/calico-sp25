#include <iostream>
#include <map>
#include <set>
#include <vector>

struct Corner
{
    int x, y;
};

struct Block
{
    Corner lowerLeft;
    Corner upperRight;
};

bool is_full_binary_tree(const std::vector<Block> &blocks)
{
    // Maps square [x, x+1] x [y, y+1] to index of block
    std::map<std::pair<int, int>, int> squareToBlockIndex;
    std::vector<std::set<int>> blocksToBlocksItIsRestingOn(blocks.size());
    std::vector<std::set<int>> blocksToBlocksRestingOnIt(blocks.size());

    for (int i = 0; i < blocks.size(); ++i) {
	for (int x = blocks[i].lowerLeft.x; x < blocks[i].upperRight.x; ++x) {
	    for (int y = blocks[i].lowerLeft.y; y < blocks[i].upperRight.y; ++y) {
		if (!squareToBlockIndex.insert({{x,y}, i}).second) {
		    // Square is covered by two blocks!
		    return false;
		}
	    }
	}
    }

    for (int i = 0; i < blocks.size(); ++i) {
	for (int y = blocks[i].lowerLeft.y; y < blocks[i].upperRight.y; ++y) {
	    if (squareToBlockIndex.find({blocks[i].lowerLeft.x - 1, y}) != squareToBlockIndex.end()) {
		// There is a block touching the left edge of this block.
		return false;
	    }
	    if (squareToBlockIndex.find({blocks[i].upperRight.x, y}) != squareToBlockIndex.end()) {
		// There is a block touching the right edge of this block.
		return false;
	    }
	}
	{
	    // Guard against lower left corner.
	    //
	    // That is, detect whether we are in the following situation:
	    //
	    //    ****
	    //    *  *
	    //    *  *
	    // *******
	    // *  *
	    // *  *
	    // ****
	    //
	    const auto it = squareToBlockIndex.find({blocks[i].lowerLeft.x - 1, blocks[i].lowerLeft.y - 1});
	    if (it != squareToBlockIndex.end()) {
		// We have another block covering the square that is touching the lower left corner in a vertex.
		// We need to make sure that we have the following situation:
		//
		//   ****
		//   *  *
		//   *  *
		// ******
		// *  *
		// *  *
		// ****
		//
		// That is, the square under lower left corner of this block is covered by the same block.
		const auto it2 = squareToBlockIndex.find({blocks[i].lowerLeft.x, blocks[i].lowerLeft.y - 1});
		if (it2 == squareToBlockIndex.end()) {
		    return false;
		}
		if (it->second != it2->second) {
		    return false;
		}
	    }
	}
	{
	    // Guard against upper left corner.
	    const auto it = squareToBlockIndex.find({blocks[i].lowerLeft.x - 1, blocks[i].upperRight.y});
	    if (it != squareToBlockIndex.end()) {
		const auto it2 = squareToBlockIndex.find({blocks[i].lowerLeft.x, blocks[i].upperRight.y});
		if (it2 == squareToBlockIndex.end()) {
		    return false;
		}
		if (it->second != it2->second) {
		    return false;
		}
	    }
	}
	{
	    // Guard against lower right corner.
	    const auto it = squareToBlockIndex.find({blocks[i].upperRight.x, blocks[i].lowerLeft.y - 1});
	    if (it != squareToBlockIndex.end()) {
		const auto it2 = squareToBlockIndex.find({blocks[i].upperRight.x - 1, blocks[i].lowerLeft.y - 1});
		if (it2 == squareToBlockIndex.end()) {
		    return false;
		}
		if (it->second != it2->second) {
		    return false;
		}
	    }
	}
	{
	    // Guard against upper right corner.
	    const auto it = squareToBlockIndex.find({blocks[i].upperRight.x, blocks[i].upperRight.y});
	    if (it != squareToBlockIndex.end()) {
		const auto it2 = squareToBlockIndex.find({blocks[i].upperRight.x - 1, blocks[i].upperRight.y});
		if (it2 == squareToBlockIndex.end()) {
		    return false;
		}
		if (it->second != it2->second) {
		    return false;
		}
	    }
	}

	// Finally, record the topology.
	for (int x = blocks[i].lowerLeft.x; x < blocks[i].upperRight.x; ++x) {
	    {
		const auto it = squareToBlockIndex.find({x, blocks[i].lowerLeft.y - 1});
		if (it != squareToBlockIndex.end()) {
		    blocksToBlocksItIsRestingOn[i].insert(it->second);
		}
	    }
	    {
		const auto it = squareToBlockIndex.find({x, blocks[i].upperRight.y});
		if (it != squareToBlockIndex.end()) {
		    blocksToBlocksRestingOnIt[i].insert(it->second);
		}
	    }
	}
    }

    // Verify topology.
    for (int i = 0; i < blocks.size(); i++) {
	const int n = blocksToBlocksItIsRestingOn[i].size();
	if (n == 0) {
	    // Either resting on floor.
	    if (blocks[i].lowerLeft.y != 0) {
		return false;
	    }
	}
	if (n > 1) {
	    // Not resting on exactly one block: fail.
	    return false;
	}
    }

    // Verify it has size of full binary tree.
    if (blocks.size() & (blocks.size() + 1)) {
	return false;
    }

    // Verify binary tree.
    for (int i = 0; i < blocks.size(); i++) {
	const std::set<int> &blocksRestingOnIt = blocksToBlocksRestingOnIt[i];
	if (i < blocks.size() / 2) {
	    if (blocksRestingOnIt != std::set<int>{ 2 * i + 1, 2 * i + 2}) {
		return false;
	    }
	} else {
	    if (!blocksRestingOnIt.empty()) {
		return false;
	    }
	}
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

	if (!is_full_binary_tree(blocks)) {
	    std::cout << "NOT A FULL BINARY TREE" << std::endl;
	    return 1;
	}
    }
    return 0;
}
