import java.io.*;
import java.util.*;

public class q_3036 {
    public static void main(String[] args) throws IOException {
 
        //1. 반복할 횟수 읽기
		BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
 
		int N = Integer.parseInt(br.readLine());
 
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
 
		//2. 첫 번째 링 반지름 읽기
		int firstRing = Integer.parseInt(st.nextToken());
 
        //3. 반복횟수만큼 나머지 반지름을 읽고,
		for (int i = 1; i < N; i++) {
			
			int otherRing = Integer.parseInt(st.nextToken());
			
			// 기약분수로 만들기 위한 최대공약수 찾기
			int gcd = gcd(firstRing, otherRing);
 
			// 분모와 분자를 최대공약수로 나눠주기 
			System.out.println(
                (firstRing / gcd) + "/" + (otherRing / gcd)
            );
		}
 
	}
 
	// 최대공약수 메소드
	static int gcd(int a, int b) {
		int r;
 
		while (b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		return a;
	}
}