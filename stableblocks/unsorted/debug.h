bool debug = true;

void
debug_begin()
{
    if (!debug) {
	return;
    }
    std::cerr << "<svg>" << std::endl;
}

void
debug_end()
{
    if (!debug) {
	return;
    }
    std::cerr << "</svg>" << std::endl;
}

void
debug_block(const Block &block)
{
    if (!debug) {
	return;
    }
    
    std::cerr
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

    std::cerr
	<< "    <line "
	<< "x1=\"" << (100.0 * x) << "\" "
	<< "y1=\"" << (-100.0 * y) << "\" "
	<< "x2=\"" << (100.0 * x) << "\" "
	<< "y2=\"" << (-100.0 * y - 50.0) << "\" "
	<< "style=\"stroke:";
    if (instable) {
	std::cerr << "red;";
    } else {
	std::cerr << "green;";
    }
    std::cerr
	<< "stroke-width:10\"/>" << std::endl;
}
