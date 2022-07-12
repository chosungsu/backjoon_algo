import java.io.*;
import java.util.*;

public class q_9375 {
    public static void main(String[] args) throws IOException{
        //1. 초기에 반복값인 T를 읽기
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
		StringBuilder sb = new StringBuilder();

        //2. T만큼 반복
        for (int i = 0; i < T; i++) {
            //3. hashmap에 상하의를 담기위해 생성
            HashMap<String, Integer> wearings = new HashMap<>();
            //4. N만큼 반복(상하의 종류 선택)
            int N = Integer.parseInt(br.readLine());
            for (int j = 0; j < N; j++) {
                st = new StringTokenizer(br.readLine(), " ");
                //5. 옷 종류는 건너뛰고 이름만 선택
                st.nextToken();
				String name = st.nextToken();

                /**
                 * 6.
				 * 해당 종류의 옷이 해시맵에 있을경우
				 * 해시맵에 저장되어있던 해당 종류의 개수를 +1 증가시킨다.
				 *
				 * 해당 종류의 옷이 해시맵에 없을 경우
				 * 해당 종류와 개수 1을 넣는다.
				 */
				
				if (wearings.containsKey(name)) {
					wearings.put(name, wearings.get(name) + 1);
				} 
				else {
					wearings.put(name, 1);
				}
            }
            int cnt = 1;
 
			/**
             * 7.
			 * 안 입는 경우를 고려하여 각 종류별 옷의 개수에 +1 해준 값을
			 * 곱해주어야 한다.
			 */
			for (int val : wearings.values()) {
				cnt *= (val + 1);
			}
			//8. 알몸인 상태를 제외해주어야 하므로 최종값에 -1이 정답.
			sb.append(cnt - 1).append('\n');
        }
        System.out.println(sb);
    }
}
