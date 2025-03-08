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
    std::map<std::pair<int, int>, int> pointToBlockIndex;
    std::vector<std::set<int>> blocksToBlocksItIsRestingOn(blocks.size());
    std::vector<std::set<int>> blocksToBlocksRestingOnIt(blocks.size());

    for (int i = 0; i < blocks.size(); ++i) {
	for (int x = blocks[i].lowerLeft.x; x < blocks[i].upperRight.x; ++x) {
	    for (int y = blocks[i].lowerLeft.y; y < blocks[i].upperRight.y; ++y) {
		if (!pointToBlockIndex.insert({{x,y}, i}).second) {
		    return false;
		}
	    }
	}
    }

    for (int i = 0; i < blocks.size(); ++i) {
	for (int y = blocks[i].lowerLeft.y; y < blocks[i].upperRight.y; ++y) {
	    if (pointToBlockIndex.find({blocks[i].lowerLeft.x - 1, y}) != pointToBlockIndex.end()) {
		return false;
	    }
	    if (pointToBlockIndex.find({blocks[i].upperRight.x, y}) != pointToBlockIndex.end()) {
		return false;
	    }
	}
	for (int x = blocks[i].lowerLeft.x; x < blocks[i].upperRight.x; ++x) {
	    {
		const auto it = pointToBlockIndex.find({x, blocks[i].lowerLeft.y - 1});
		if (it != pointToBlockIndex.end()) {
		    blocksToBlocksItIsRestingOn[i].insert(it->second);
		}
	    }
	    {
		const auto it = pointToBlockIndex.find({x, blocks[i].upperRight.y});
		if (it != pointToBlockIndex.end()) {
		    blocksToBlocksRestingOnIt[i].insert(it->second);
		}
	    }
	}
    }

    for (int i = 0; i < blocks.size(); i++) {
	const int n = blocksToBlocksItIsRestingOn[i].size();
	if (n == 0) {
	    if (blocks[i].lowerLeft.y != 0) {
		return false;
	    }
	}
	if (n > 1) {
	    return false;
	}
    }

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

    if (blocks.size() & (blocks.size() + 1)) {
	return false;
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
