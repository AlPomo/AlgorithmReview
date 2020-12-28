import java.util.*;
import java.io.*;
 
public class Main {
    static int N;
    static int K;
    static int[] weights;
    static int[] values;
 
    public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        StringTokenizer st = new StringTokenizer(br.readLine());
    	N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        weights = new int[N];
        values = new int[N];
 
        for (int i = 0; i < N; i++) {
        	st = new StringTokenizer(br.readLine());
        	weights[i] = Integer.parseInt(st.nextToken());
            values[i] = Integer.parseInt(st.nextToken());
        }
        memo = new int[N][K+1];
        for(int i = 0; i < N; i++)
        	Arrays.fill(memo[i], -1);
        
        System.out.print(dfs(0, 0));
        
    }
    static int[][] memo;
    static int dfs(int idx, int weight) {
        if (idx == N) {
            return 0;
        }
        if(memo[idx][weight] != -1 )
            return memo[idx][weight];
        // 못담음
        if (weight + weights[idx] > K) {
            memo[idx][weight] = dfs(idx + 1, weight);
            return memo[idx][weight];
        } else
            memo[idx][weight] = Math.max(
                    dfs(idx + 1, weight), 
                    values[idx] + dfs(idx + 1, weight + weights[idx]));
            return memo[idx][weight];
    }
}
