import java.io.*;
import java.util.*;
public class Main {
	static boolean[][] visited;
	static int N;
	static int[][] map;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		for(int i=0; i<N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j=0; j<N; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		list = new HashSet<>();
		visited = new boolean[N][N];
		int a = 1;
		for(int i=0; i<map.length; i++) {
			for(int j=0; j<map[i].length; j++) {
				if(!visited[i][j] && map[i][j]==1) {
					bfs(i, j, a);
					map[i][j]=a;
					a++;
				}
			}
		}
		answer = Integer.MAX_VALUE;
		List<Node> real = new ArrayList<>(list);
		for(int i=0; i<real.size(); i++) {
			Node poll = real.get(i);
			bridge(poll);
		}
		System.out.print(answer);
	}
	static void bridge(Node f) {
		Queue<Node> queue = new LinkedList<>();
		boolean[][] visited = new boolean[N][N];
        visited[f.r][f.c] = true;
		queue.add(f);
		
		while(!queue.isEmpty()) {
			int size = queue.size();
			for(int s=0; s<size; s++) {
				Node poll = queue.poll();
				if(poll.len>answer) return;
				
				for(int i=0; i<4; i++) {
					int nr = poll.r + dr[i];
					int nc = poll.c + dc[i];
					
					if(nr>=0 && nr<N && nc>=0 && nc<N && !visited[nr][nc]) {
						if(poll.num!=map[nr][nc]) {
							if(map[nr][nc]>0) {
								answer = Math.min(answer, poll.len);
								return;
							}
							queue.add(new Node(nr, nc, poll.num, poll.len+1));
							visited[nr][nc]=true;
						}
					}
					
				}
			}
		}
		
	}
	static int answer;
	static Set<Node> list;
	static int[] dr = {0,0,1,-1};
	static int[] dc = {1,-1,0,0};
	static void bfs(int r, int c, int a) {
		Queue<Node> queue = new LinkedList<>();
		queue.add(new Node(r, c, a, 0));
		
		while(!queue.isEmpty()) {
			Node poll = queue.poll();
			visited[poll.r][poll.c]=true;
			
			for(int i=0; i<4; i++) {
				int nr = poll.r + dr[i];
				int nc = poll.c + dc[i];
				
				if(nr>=0 && nr<N && nc>=0 && nc<N) {
					if(!visited[nr][nc]) {
						if(map[nr][nc]==1) {
                            queue.add(new Node(nr, nc, a, 0));
						    map[nr][nc]=poll.num;
                        } else if(map[nr][nc]==0) {
                            list.add(poll);
                        }
						visited[nr][nc]=true;
					}
				}
			}
		}
	}
	static class Node{
		int r, c, num, len;
		Node(int r, int c, int num, int len) {
			this.r=r;
			this.c=c;
			this.num=num;
			this.len=len;
		}
	}
}
