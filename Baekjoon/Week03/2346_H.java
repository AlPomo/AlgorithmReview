import java.util.*;
import java.io.*;
public class Main {
	static class Node {
		int idx;
		int value;
		Node(int value, int idx) {
			this.value = value;
			this.idx = idx;
		}
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		List<Node> list = new LinkedList<>();
		for(int n=0; n<N; n++) {
			list.add(new Node(Integer.parseInt(st.nextToken()), n+1));
		}
		int nextIdx = 0, reIdx = 0;
		StringBuilder sb = new StringBuilder();
		while(list.size()!=1) {
			sb.append(list.get(reIdx).idx).append(" ");
			nextIdx = reIdx + list.get(reIdx).value;
			list.remove(reIdx);
			reIdx=reIdx<nextIdx?nextIdx-1:nextIdx;
			while(reIdx<0) reIdx = reIdx + list.size();
			reIdx %= list.size();
		}
		sb.append(list.get(0).idx);
		System.out.print(sb);
	}
}