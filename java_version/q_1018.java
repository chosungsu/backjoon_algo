package java_version;
import java.util.*;
public class q_1018 {
    public static boolean[][] arr;
    public static int min = 64;

    public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        arr = new boolean[N][M];

        //배열 입력
        for (int i = 0; i < N; i++) {
            String str = sc.next();
            for (int j = 0; j < M; j++) {
                if (str.charAt(j) == 'W') {
                    arr[i][j] = true;
                } else {
                    arr[i][j] = false;
                }
            }
        }

        int N_row = N - 7;
        int M_col = M - 7;
        for (int i = 0; i < N_row; i++) {
            for (int j = 0; j < M_col; j++) {
                find(i, j);
            }
        }
        System.out.println(min);
	}

    public static void find(int x, int y) {
        int end_x = x + 8;
        int end_y = y + 8;
        int count = 0;
        boolean color = arr[x][y];

        for (int i = x; i < end_x; i++) {
            for (int j = y; j < end_y; j++) {
                //올바른 색이 아닌 경우
                if (arr[i][j] != color) {
                    count ++;
                }
                //다음칸을 위한 색깔 불린값 변경
                color = !color;
            }
            color = !color;
        }
        count = Math.min(count, 64 - count);
        min = Math.min(min, count);
    }
}