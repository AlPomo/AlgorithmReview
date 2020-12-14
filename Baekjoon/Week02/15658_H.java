import java.util.*;
import java.io.*;
public class Main {
	static int[] num;
	static int N, min=Integer.MAX_VALUE, max=Integer.MIN_VALUE;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		num = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int n=0; n<N; n++) num[n] = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		dfs(1, num[0], Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		System.out.println(max);
		System.out.print(min);
	}
	
	static void dfs(int numIdx, int sum, int a, int b, int c, int d) {
		if(numIdx==N) {
			min = Math.min(min, sum);
			max = Math.max(max, sum);
			return;
		}
		if(a>0) dfs(numIdx+1, sum+num[numIdx], a-1, b, c, d);
		if(b>0) dfs(numIdx+1, sum-num[numIdx], a, b-1, c, d);
		if(c>0) dfs(numIdx+1, sum*num[numIdx], a, b, c-1, d);
		if(d>0) dfs(numIdx+1, sum/num[numIdx], a, b, c, d-1);
	}
}
