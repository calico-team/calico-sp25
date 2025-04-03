import java.io.*;

class Solution {
    static boolean is_stable(int[][][] blocks) {
        // YOUR CODE HERE
	return true;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
	int numCases = Integer.parseInt(in.readLine());
	for (int i = 0; i < numCases; ++i) {
	    int numBlocks = Integer.parseInt(in.readLine());
	    int[][][] blocks = new int[numBlocks][2][2];
	    for (int b = 0; b < numBlocks; ++b) {
		String[] temp = in.readLine().split(" ");
		blocks[b][0][0] = Integer.parseInt(temp[0]);
		blocks[b][0][1] = Integer.parseInt(temp[1]);
		blocks[b][1][0] = Integer.parseInt(temp[2]);
		blocks[b][1][1] = Integer.parseInt(temp[3]);
	    }
	    if (is_stable(blocks)) {
		out.println("Stable");
	    } else {
		out.println("Unstable");
	    }
	}
	out.flush();
    }
}
