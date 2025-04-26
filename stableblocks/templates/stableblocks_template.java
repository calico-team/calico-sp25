import java.io.*;

class Solution {
    static boolean is_stable(int[][][] blocks) {
        // YOUR CODE HERE
	return true;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
	int T = Integer.parseInt(in.readLine());
	for (int j = 0; j < T; ++j) {
	    int N = Integer.parseInt(in.readLine());
	    int[][][] blocks = new int[N][2][2];
	    for (int i = 0; i < N; ++i) {
		String[] temp = in.readLine().split(" ");
		blocks[i][0][0] = Integer.parseInt(temp[0]);
		blocks[i][0][1] = Integer.parseInt(temp[1]);
		blocks[i][1][0] = Integer.parseInt(temp[2]);
		blocks[i][1][1] = Integer.parseInt(temp[3]);
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
