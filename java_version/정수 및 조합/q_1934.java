import java.io.*;
import java.util.*;

public class q_1934 {
    public static void main(String[] args) throws IOException {
 
        //반복할 횟수 읽기
		BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
 
        int N = Integer.parseInt(br.readLine());

		StringTokenizer st;
		
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
		    int b = Integer.parseInt(st.nextToken());
            int d = gcd(a, b);
            System.out.println(a*b/d);
        }
	}
 
	// 최대공약수 반복문 방식
	public static int gcd(int a, int b) {
 
		while (b != 0) {
			int r = a % b; // 나머지를 구해준다.
 
			// GCD(a, b) = GCD(b, r)이므로 변환한다.
			a = b;
			b = r;
		}
		return a;
	}
}
