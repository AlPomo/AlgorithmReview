import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int[] a = new int[N];
		st = new StringTokenizer(br.readLine());
		a[0] = Integer.parseInt(st.nextToken());
		for(int i=1; i<N; i++) {
			a[i] = a[i-1] + Integer.parseInt(st.nextToken());
		}
		int ans = a[K-1];
		for(int i=K; i<N; i++) {
			ans = Math.max(ans, a[i]-a[i-K]);
		}
		System.out.print(ans);
	}
}
