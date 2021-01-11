import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] map = new int[N][N];
        cnt = 0;
        backtrack(map, 0);
        System.out.println(cnt);
    }
    static int cnt;
    static void backtrack(int[][] map, int idx) {
        if( idx == map.length ) {
            cnt++;
            return;
        }
        for(int i = 0; i < map[idx].length; i++) {
             
            if( canBeNQueen(map, idx, i) ) {
                map[idx][i] = 1;
                backtrack(map, idx+1);
                map[idx][i] = 0;
            }
        }
    }
    static boolean canBeNQueen(int[][] map, int r, int c) {
        for(int i = r - 1; i >= 0; i--) {
            if( map[i][c] == 1 )
                return false;
        }
        for(int i = r-1, j = c-1; i >= 0 && j >= 0; i--, j--) {
            if(map[i][j] == 1)
                return false;
        }
        for(int i = r-1, j = c+1; i >= 0 && j < map[i].length; i--, j++) {
            if(map[i][j] == 1)
                return false;
        }
        return true;
    }
}
