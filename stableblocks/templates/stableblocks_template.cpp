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
    // YOUR CODE HERE
    return true;
}

int main()
{
    int T;
    std::cin >> T;

    for (int j = 0; j < T; j++) {
	int N;
	std::cin >> N;

	std::vector<Block> blocks;

	for (int i = 0; i < N; i++) {
	    Block block;
	    std::cin >> block.lowerLeft.x >> block.lowerLeft.y
		     >> block.upperRight.x >> block.upperRight.y;
	    blocks.push_back(block);
	}

	if (is_stable(blocks)) {
	    std::cout << "Stable" << std::endl;
	} else {
	    std::cout << "Unstable" << std::endl;
	}
    }
}
