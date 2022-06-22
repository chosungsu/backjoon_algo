import java.io.*;
import java.util.*;

public class q_1269 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 1. a, b 집합 개수 읽기
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        Set<Integer> setA = new HashSet<>();
        Set<Integer> setB = new HashSet<>();

        // 2. 집합 개수만큼 set에 담기
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < a; i++) {
            setA.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < b; i++) {
            setB.add(Integer.parseInt(st.nextToken()));
        }

        int ans = 0;
        // 3. a집합의 원소가 b집합에 없을 경우
        for(int num : setA) {
            if(!setB.contains(num)) {
                ans += 1;
            }
        }
        // 4. b집합의 원소가 a집합에 없을 경우
        for(int num : setB) {
            if(!setA.contains(num)) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }
}
