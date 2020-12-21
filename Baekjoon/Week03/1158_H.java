import java.util.*;
import java.io.*;
public class Main {
	public static String Solution(int N, int K) {
		StringBuilder sb = new StringBuilder();
		sb.append("<");
		ArrayList<Integer> list = new ArrayList<>();
		for(int i=1; i<=N; i++) list.add(i);
		int idx = 0;
		while(list.size()!=1) {
			idx = ((idx + K -1) + N) % N;
			sb.append(list.get(idx)).append(", ");
			list.remove(idx);
			N--;
		}
		return sb.append(list.get(0)).append(">").toString();
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		System.out.print(Solution(N, K));
	}
}
