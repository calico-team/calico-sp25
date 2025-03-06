#include <fstream>

bool debug = true;

int c = 0;
std::ofstream f;

void
debug_begin()
{
    if (!debug) {
	return;
    }

    const std::string filename =
	"blocks_" + std::to_string(c) + ".svg";
    
    f.open(filename.c_str());
    
    f << "<svg>" << std::endl;
}

void
debug_end()
{
    if (!debug) {
	return;
    }
    f << "</svg>" << std::endl;

    f.close();
    
    c++;
}

void
debug_block(const Block &block)
{
    if (!debug) {
	return;
    }
    
    f
	<< "    <polygon points=\""
	<< 100 * block.lowerLeft.x << "," << -100 * block.lowerLeft.y << " "
	<< 100 * block.lowerLeft.x << "," << -100 * block.upperRight.y << " "
	<< 100 * block.upperRight.x << "," << -100 * block.upperRight.y << " "
	<< 100 * block.upperRight.x << "," << -100 * block.lowerLeft.y << "\" "
	<< "style=\"fill:none;stroke:black;stroke-width:5\"/>" << std::endl;
}

void
debug_center(const double x, const double y, const bool instable)
{
    if (!debug) {
	return;
    }

    f
	<< "    <line "
	<< "x1=\"" << (100.0 * x) << "\" "
	<< "y1=\"" << (-100.0 * y) << "\" "
	<< "x2=\"" << (100.0 * x) << "\" "
	<< "y2=\"" << (-100.0 * y - 50.0) << "\" "
	<< "style=\"stroke:";
    if (instable) {
	f << "red;";
    } else {
	f << "green;";
    }
    f
	<< "stroke-width:10\"/>" << std::endl;
}
