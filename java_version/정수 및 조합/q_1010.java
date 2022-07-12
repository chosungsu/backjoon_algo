import java.io.*;
import java.util.*;

public class q_1010 {
    //1. 변수 생성
    //문제 제한조건인 n, m이 모두 30미만이므로 아래와 같이 생성함
    static int[][] dp = new int[30][30];
    public static void main(String[] args) throws IOException{

        //2. 초기에 반복할 T를 읽기
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
		StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        //3. T만큼 반복하기
		for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            sb.append(Combi(M, N)).append('\n');
        }
        System.out.println(sb);
    }
    static int Combi(int M, int N) {
        // 이미 풀린 경우 바로 반환
		if(dp[M][N] > 0) {
			return dp[M][N]; 
		}
		
		// 2번 성질
		if(M == N || N == 0) {
			return dp[M][N] = 1;
		}
		
		// 1번 성질
		return dp[M][N] = Combi(M - 1, N - 1) + Combi(M - 1, N);
    }
}
