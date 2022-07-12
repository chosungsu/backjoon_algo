import java.io.*;
import java.util.*;

public class q_2981 {
    public static void main(String[] args) throws IOException {
 
        //반복할 횟수 읽기
		BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
        //1. 계산할 숫자를 행렬에 담기
		int[] arr = new int[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
 
        //2. 배열을 정렬한다
		Arrays.sort(arr);
        //3. 음수가 되지 않도록 큰 수에서 작은 수로 빼준다.
		int gcdVal = arr[1] - arr[0];
 
        //4. 직전의 최대 공약수와 다음 수(arr[i] - arr[i - 1])의 최대공약수를 갱신 
		for(int i = 2; i < N; i++) {
			
			gcdVal = gcd(gcdVal, arr[i] - arr[i - 1]);
		}
 
		//5. 최대공약수의 약수들 찾기
		for(int i = 2; i <= gcdVal; i++) {
	    
			if(gcdVal % i == 0) {
				System.out.print(i + " ");
			}
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
