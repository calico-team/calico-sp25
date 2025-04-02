#include <iostream>
#include <vector>

using namespace std;

struct Corner
{
    int x, y;
};

struct Block
{
    Corner lowerLeft;
    Corner upperRight;
};

bool is_stable(const vector<Block> &blocks)
{
    // Write code here.
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

	if (is_stable(blocks)) {
	    std::cout << "Stable" << std::endl;
	} else {
	    std::cout << "Unstable" << std::endl;
	}
    }
}
