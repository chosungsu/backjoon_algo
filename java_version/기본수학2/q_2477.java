import java.io.*;
import java.util.*;

public class q_2477 {
    public static void main(String[] args) throws Exception{
		BufferedReader br =new BufferedReader(
            new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
        // 1. 제곱미터 당 참외 개수
		int K = Integer.parseInt(st.nextToken()); 
		
        // 2. 라인별 동서남북 숫자와 길이 읽기
		st = new StringTokenizer(br.readLine());
		st.nextToken();
        //3. 첫번째 변은 마지막 변과 곱해주어야 하므로 따로 처리
		int a = Integer.parseInt(st.nextToken()); 
		int before = a;

		int max = 0;
		int sum = 0;

        //4. 나머지 변을 반복문으로 처리
		for(int i = 1 ; i < 6 ; i++) {
			st = new StringTokenizer(br.readLine());
			st.nextToken();
			int now = Integer.parseInt(st.nextToken());
            // 최댓값은 인접한 변의 곱 중 하나이다.
			max = Math.max(now*before, max); 
            // 넓이의 합 구하기
			sum += now*before;
            // 이전 변을 지금 변으로 변환
			before = now;	
		}
        // 마지막 변과 첫번째 변 곱해줌
		sum+= a*before; 
        // 마지막변과 첫번째 변 크기 체크
		max = Math.max(a*before, max); 
		
		// 3*max - sum : 빈 부분의 넓이
		int result = (max- (3*max - sum))*K;  
		System.out.println(result);
	}
}
